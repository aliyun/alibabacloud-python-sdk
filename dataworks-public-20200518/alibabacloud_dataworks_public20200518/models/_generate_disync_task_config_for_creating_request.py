# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDISyncTaskConfigForCreatingRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: int = None,
        task_param: str = None,
        task_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. This parameter is used to prevent repeated operations that are caused by multiple calls.
        self.client_token = client_token
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The script for the synchronization task. DataWorks allows you to create the following types of synchronization tasks:
        # 
        # *   Synchronization task that is used to synchronize data from MySQL to MaxCompute
        # *   Synchronization task that is used to synchronize data from MySQL data to Kafka
        # *   Synchronization task that is used to synchronize data from MySQL to Hologres
        # 
        # The SelectedTables parameter is used to specify tables that you want to synchronize from multiple databases. The Tables parameter is used to specify tables that you want to synchronize from a single database.
        # 
        # *   If the script contains the SelectedTables parameter, the system synchronizes data from the tables that you specify in the SelectedTables parameter.
        # *   If the script contains the Tables parameter, the system synchronizes data from the tables that you specify in the Tables parameter.
        # 
        # The following sample code provides a script for data synchronization from MySQL to MaxCompute:
        # 
        #     {
        #       "type": "realtime",
        #       "version": "1.0",
        #       "setting": {
        #         "resourceGroup": "S_res_group_280749521950784_1623033752022",
        #         "taskType": "oneclick_to_odps"
        #       },
        #       "steps": [
        #         {
        #           "stepType": "mysql",
        #           "parameter": {
        #             "connection": [
        #               {
        #                 "datasourceType": "mysql",
        #                 "datasource": "mysql_pub1",
        #                 "selectedTables": [
        #                   {
        #                     "dbName": "mysql_db",
        #                     "schema": [
        #                       {
        #                         "tableInfos": [
        #                           {
        #                             "table": "molin_di_test_in_pk_v4"
        #                           }
        #                         ]
        #                       }
        #                     ]
        #                   }
        #                 ]
        #               }
        #             ]
        #           },
        #           "name": "Reader",
        #           "category": "reader"
        #         },
        #         {
        #           "stepType": "odps",
        #           "parameter": {
        #             "datasource": "odps_source"
        #           },
        #           "name": "Writer",
        #           "category": "writer"
        #         }
        #       ]
        #     }
        # 
        # The following sample code provides a script for data synchronization from MySQL to Kafka:
        # 
        #     {
        #       "type": "realtime",
        #       "version": "1.0",
        #       "setting": {
        #         "resourceGroup": "S_res_group_280749521950784_1623033752022",
        #         "taskType": "oneclick_to_kafka"
        #       },
        #       "steps": [
        #         {
        #           "stepType": "mysql",
        #           "parameter": {
        #             "connection": [
        #               {
        #                 "datasourceType": "mysql",
        #                 "datasource": "pkset_test",
        #                 "selectedTables": [
        #                   {
        #                     "dbName": "mysql_db",
        #                     "schema": [
        #                       {
        #                         "tableInfos": [
        #                           {
        #                             "table": "molin_di_test_in_pk_v4"
        #                           }
        #                         ]
        #                       }
        #                     ]
        #                   }
        #                 ]
        #               }
        #             ]
        #           },
        #           "name": "Reader",
        #           "category": "reader"
        #         },
        #         {
        #           "stepType": "kafka",
        #           "parameter": {
        #             "datasource": "azn_kafka"
        #           },
        #           "name": "Writer",
        #           "category": "writer"
        #         }
        #       ]
        #     }
        # 
        # The following sample code provides a script for data synchronization from MySQL to Hologres:
        # 
        #     {
        #       "type": "realtime",
        #       "version": "1.0",
        #       "setting": {
        #         "resourceGroup": "S_res_group_280749521950784_1623033752022",
        #         "taskType": "oneclick_to_holo"
        #       },
        #       "steps": [
        #         {
        #           "stepType": "mysql",
        #           "parameter": {
        #             "connection": [
        #               {
        #                 "datasourceType": "mysql",
        #                 "datasource": "mysql_pub",
        #                 "selectedTables": [
        #                   {
        #                     "dbName": "mysql_db",
        #                     "schema": [
        #                       {
        #                         "tableInfos": [
        #                           {
        #                             "table": "molin_di_test_in2_pk_v3"
        #                           }
        #                         ]
        #                       }
        #                     ]
        #                   }
        #                 ]
        #               }
        #             ]
        #           },
        #           "name": "Reader",
        #           "category": "reader"
        #         },
        #         {
        #           "stepType": "holo",
        #           "parameter": {
        #             "datasource": "holo"
        #           },
        #           "name": "Writer",
        #           "category": "writer"
        #         }
        #       ]
        #     }
        # 
        # This parameter is required.
        self.task_param = task_param
        # The type of task that you want to create in Data Integration in asynchronous mode. Valid values:
        # 
        # *   DI_REALTIME: real-time synchronization task
        # *   DI_SOLUTION: another type of synchronization task
        # 
        # DataWorks allows you to create real-time synchronization tasks and other types of synchronization tasks in Data Integration only in asynchronous mode.
        # 
        # *   DI_OFFLINE
        # *   DI_REALTIME
        # *   DI_SOLUTION
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

