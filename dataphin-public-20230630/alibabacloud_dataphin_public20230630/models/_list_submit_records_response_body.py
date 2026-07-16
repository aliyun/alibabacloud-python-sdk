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
        # Error code. OK indicates a successful request.
        self.code = code
        # HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # Query result.
        self.list_result = list_result
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether the request is successful.
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
        # List of pending deployment records.
        self.data = data
        # Total count.
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
        # Change type. 0: Create / 1: Update / 2: Delete.
        self.change_type = change_type
        # Creation time in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # Modification time in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_modify = gmt_modify
        # Pending deployment record ID.
        self.id = id
        # Node ID.
        self.node_id = node_id
        # Object ID.
        self.object_id = object_id
        # Object name.
        self.object_name = object_name
        # Object type. Valid values:
        # - MaxCompute SQL task: MAX_COMPUTE_SQL
        # - MaxCompute MR task: MAX_COMPUTE_MR
        # - Spark JAR on MaxCompute: SPARK_JAR_ON_MAX_COMPUTE
        # - Shell task: SHELL
        # - Python task: PYTHON
        # - Perl script: PERL
        # - Check: CHECK
        # - Sync task: DATA_X
        # - Virtual node: VIRTUAL
        # - Resource: IDE_RESOURCE
        # - Function: UDF
        # - Hive SQL task: HIVE_SQL
        # - Hadoop MR task: HADOOP_MR
        # - Spark JAR on Hive task: SPARK_JAR_ON_HIVE
        # - Flink SQL task: FLINK_SQL
        # - Flink SQL template task: FLINK_TEMPLATE_SQL
        # - Stream computing template: STREAM_TEMPLATE
        # - Metatable: META_TABLE
        # - Stream computing function: STREAM_UDF
        # - Real-time Flink DataStream: FLINK_DATASTREAM
        # - Real-time custom data source: STREAM_CUSTOM_DATASOURCE
        # - AnalyticDB for PostgreSQL task: ADB_FOR_PG
        # - TDH SQL task: INCEPTOR_SQL
        # - Mirror table: MIRROR_TABLE
        # - Intermediate table: MIDDLE_TABLE
        # - Application table: APPLICATION_TABLE
        # - Impala SQL task: IMPALA_SQL
        # - Offline pipeline task: OFFLINE_PIPELINE
        # - Real-time pipeline task: REAL_TIME_PIPELINE
        # - Dimension logical table: DIM_LOGICAL_TABLE
        # - Fact logical table: FCT_LOGICAL_TABLE
        # - Business condition: BIZ_CONDITION
        # - Atomic metric: ATOM_INDEX
        # - Derived metric: DERIVED_INDEX
        # - Calculated derived metric: CALC_DERIVED_INDEX
        # - PAI task: PAI_DESIGNER
        # - ArgoDB SQL task: ARGODB_SQL
        # - Hologres SQL task: HOLOGRES_SQL
        # - Impala SQL task: IMPALA_SQL
        # - StarRocks SQL task: STARROCKS_SQL
        # - Database SQL task: DATABASE_SQL
        # - Spark SQL task: SPARK_SQL
        # - Compute template: TASK_TEMPLATE
        # - External trigger node: EXTERNAL_TRIGGER
        # - Gauss SQL task: GAUSS_SQL
        self.object_type = object_type
        # Object version.
        self.object_version = object_version
        # Project ID.
        self.project_id = project_id
        # Submission comment.
        self.submit_comment = submit_comment
        # Submitter ID.
        self.submitter = submitter
        # Submitter name.
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

