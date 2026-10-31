# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSubmitRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list_result: main_models.ListSubmitRecordsResponseBodyListResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of OK indicates that the request is successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The query result.
        self.list_result = list_result
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.list_result:
            self.list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.list_result is not None:
            result['ListResult'] = self.list_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ListResult') is not None:
            temp_model = main_models.ListSubmitRecordsResponseBodyListResult()
            self.list_result = temp_model.from_map(m.get('ListResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSubmitRecordsResponseBodyListResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSubmitRecordsResponseBodyListResultData] = None,
        total_count: int = None,
    ):
        # The list of pending publish records.
        self.data = data
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSubmitRecordsResponseBodyListResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSubmitRecordsResponseBodyListResultData(DaraModel):
    def __init__(
        self,
        change_type: int = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        id: int = None,
        node_id: str = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_version: str = None,
        project_id: str = None,
        submit_comment: str = None,
        submitter: str = None,
        submitter_name: str = None,
    ):
        # The change type. Valid values:
        # - 0: create
        # - 1: update
        # - 2: delete
        self.change_type = change_type
        # The time when the record was created. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_create = gmt_create
        # The time when the record was updated. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_modify = gmt_modify
        # The ID of the pending publish record.
        self.id = id
        # The ID of the node.
        self.node_id = node_id
        # The ID of the object.
        self.object_id = object_id
        # The name of the object.
        self.object_name = object_name
        # The object type. Valid values:
        # - MAX_COMPUTE_SQL: MaxCompute SQL node
        # - MAX_COMPUTE_MR: MaxCompute MR node
        # - SPARK_JAR_ON_MAX_COMPUTE: Spark JAR on MaxCompute node
        # - SHELL: Shell node
        # - PYTHON: Python node
        # - PERL: Perl script
        # - CHECK: Check node
        # - DATA_X: Data synchronization node
        # - VIRTUAL: Virtual node
        # - IDE_RESOURCE: Resource
        # - UDF: Function
        # - HIVE_SQL: Hive SQL node
        # - HADOOP_MR: Hadoop MR node
        # - SPARK_JAR_ON_HIVE: Spark JAR on Hive node
        # - FLINK_SQL: Flink SQL node
        # - FLINK_TEMPLATE_SQL: Flink SQL template node
        # - STREAM_TEMPLATE: Stream computing template
        # - META_TABLE: Metatable
        # - STREAM_UDF: Stream computing function
        # - FLINK_DATASTREAM: Real-time Flink DataStream node
        # - STREAM_CUSTOM_DATASOURCE: Real-time custom data source
        # - ADB_FOR_PG: AnalyticDB for PostgreSQL node
        # - INCEPTOR_SQL: Inceptor SQL node
        # - MIRROR_TABLE: Mirror table
        # - MIDDLE_TABLE: Intermediate table
        # - APPLICATION_TABLE: Application table
        # - IMPALA_SQL: Impala SQL node
        # - OFFLINE_PIPELINE: Offline pipeline node
        # - REAL_TIME_PIPELINE: Real-time pipeline node
        # - DIM_LOGICAL_TABLE: Logical dimension table
        # - FCT_LOGICAL_TABLE: Logical fact table
        # - BIZ_CONDITION: Business filter
        # - ATOM_INDEX: Atomic metric
        # - DERIVED_INDEX: Derived metric
        # - CALC_DERIVED_INDEX: Derivative metric
        # - PAI_DESIGNER: PAI Designer node
        # - ARGODB_SQL: ArgoDB SQL node
        # - HOLOGRES_SQL: Hologres SQL node
        # - IMPALA_SQL: Impala SQL node
        # - STARROCKS_SQL: StarRocks SQL node
        # - DATABASE_SQL: Database SQL node
        # - SPARK_SQL: Spark SQL node
        # - TASK_TEMPLATE: Task template
        # - EXTERNAL_TRIGGER: External trigger node
        # - GAUSS_SQL: Gauss SQL node
        self.object_type = object_type
        # The version of the object.
        self.object_version = object_version
        # The project ID.
        self.project_id = project_id
        # The submission comment.
        self.submit_comment = submit_comment
        # The ID of the submitter.
        self.submitter = submitter
        # The name of the submitter.
        self.submitter_name = submitter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.id is not None:
            result['Id'] = self.id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.submit_comment is not None:
            result['SubmitComment'] = self.submit_comment

        if self.submitter is not None:
            result['Submitter'] = self.submitter

        if self.submitter_name is not None:
            result['SubmitterName'] = self.submitter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubmitComment') is not None:
            self.submit_comment = m.get('SubmitComment')

        if m.get('Submitter') is not None:
            self.submitter = m.get('Submitter')

        if m.get('SubmitterName') is not None:
            self.submitter_name = m.get('SubmitterName')

        return self

