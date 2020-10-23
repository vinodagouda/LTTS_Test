# LTTS_Test
Quick API in less than 30 mins.

from employee.tasks import add

add.delay(4,4)
#<AsyncResult: 1708e744-c76d-4866-8e27-ecd51db0182d>

#[2020-10-23 05:15:48,218: INFO/ForkPoolWorker-2] Task #employee.tasks.add[1708e744-c76d-4866-8e27-ecd51db0182d] succeeded in 0.00032939700031420216s: 8


add.apply_async((9,9), countdown=10)
#<AsyncResult: 5522a7ac-ff2f-49c9-b36b-b4b744c82172>

#[2020-10-23 05:20:34,958: INFO/MainProcess] Received task: #employee.tasks.add[5522a7ac-ff2f-49c9-b36b-b4b744c82172]  ETA:[2020-10-23 05:20:44.954298+00:00] 
#[2020-10-23 05:20:45,234: INFO/ForkPoolWorker-2] Task #employee.tasks.add[5522a7ac-ff2f-49c9-b36b-b4b744c82172] succeeded in 0.0002630729995871661s: 18
