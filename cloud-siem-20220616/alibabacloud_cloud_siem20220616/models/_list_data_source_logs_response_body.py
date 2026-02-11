# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceLogsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataSourceLogsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataSourceLogsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourceLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: List[main_models.ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs] = None,
        data_source_instance_name: str = None,
        data_source_instance_remark: str = None,
        sub_user_id: int = None,
    ):
        # The ID of the cloud account.
        self.account_id = account_id
        # The code that is used for multi-cloud environments. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        # The ID of the data source. The value is obtained after the threat analysis feature calculates the MD5 hash value of a parameter.
        self.data_source_instance_id = data_source_instance_id
        # The logs of the data source.
        self.data_source_instance_logs = data_source_instance_logs
        # The name of the data source.
        self.data_source_instance_name = data_source_instance_name
        # The remarks of the data source.
        self.data_source_instance_remark = data_source_instance_remark
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.data_source_instance_logs:
            for v1 in self.data_source_instance_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id

        result['DataSourceInstanceLogs'] = []
        if self.data_source_instance_logs is not None:
            for k1 in self.data_source_instance_logs:
                result['DataSourceInstanceLogs'].append(k1.to_map() if k1 else None)

        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name

        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')

        self.data_source_instance_logs = []
        if m.get('DataSourceInstanceLogs') is not None:
            for k1 in m.get('DataSourceInstanceLogs'):
                temp_model = main_models.ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs()
                self.data_source_instance_logs.append(temp_model.from_map(k1))

        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')

        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs(DaraModel):
    def __init__(
        self,
        log_code: str = None,
        log_instance_id: str = None,
        log_mds_code: str = None,
        log_params: List[main_models.ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams] = None,
        task_status: int = None,
    ):
        # The code of the log.
        self.log_code = log_code
        # The ID of the log. The value is obtained after the threat analysis feature calculates the MD5 hash value of a parameter.
        self.log_instance_id = log_instance_id
        # The display code of the log.
        self.log_mds_code = log_mds_code
        # The parameters of the log.
        self.log_params = log_params
        # Indicates whether the task for which logs are collected is enabled. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.task_status = task_status

    def validate(self):
        if self.log_params:
            for v1 in self.log_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id

        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code

        result['LogParams'] = []
        if self.log_params is not None:
            for k1 in self.log_params:
                result['LogParams'].append(k1.to_map() if k1 else None)

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')

        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')

        self.log_params = []
        if m.get('LogParams') is not None:
            for k1 in m.get('LogParams'):
                temp_model = main_models.ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams()
                self.log_params.append(temp_model.from_map(k1))

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams(DaraModel):
    def __init__(
        self,
        para_code: str = None,
        para_value: str = None,
    ):
        # The parameter code of the log.
        self.para_code = para_code
        # The parameter value of the log.
        self.para_value = para_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.para_code is not None:
            result['ParaCode'] = self.para_code

        if self.para_value is not None:
            result['ParaValue'] = self.para_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')

        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')

        return self

