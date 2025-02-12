Source: https://seddonym.me/2020/11/19/trouble-atomic/

``` python
def transfer_money():
	with transaction.atomic():
		CreditLine.objects.create(...)
		CreditTransh.objects.create(...)
		api.send_transh(...)
```
This code is absolutely fine. If api call fails we don't commit anything and if we don't write to database, we don't calll api.

### But
If we call this function inside another transactional function
``` python
def issue_credit():
	with transaction.atomic():
		transfer_money()
		applciation = Application.objects.select_for_update()
		application.status = "issued"
		application.save()
```
And this outer transaction fails because of any error (connection, integrity e.t.c.) we get a consistency issue or **Durability** issue because we've already sent transh to api.


## SO
To prevent `transfer_money()` function to be called within another transaction we should make inner transaction `durable`. So when it is called inside of another outer transaction, an error would be raised to prevent developer from using `nested` transaction with this function.

``` python
def issue_credit():
	with transaction.atomic(durable=True):
		transfer_money()
		applciation = Application.objects.select_for_update()
		application.status = "issued"
		application.save()
```
NOTE: Since Django3.2
## Unfortunately 
It doesn't solve a problem with transfer money_function because a timeout could occur on api or a database may loose connection before we commit but when the api was already called. To solve this problem we use idempotency and retry mechanisms


## Test durable atomic function
We should inherit all tests with durable functions from
`django.test.TransactionTestCase`

because by default django tests run inside of transactions, which ensures consistency and performance (transactional tests run a way faster, so we should use them most of the time) but they would **raise a n error** for durable functions and don't catch errors related to **selected_for_update** outside of transaction

## Nested transactions are not supported in databases like postgresql

So Django uses save points to implement them