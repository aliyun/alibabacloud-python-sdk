# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterConfigChangeLogsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.DescribeDBClusterConfigChangeLogsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The information returned.
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBClusterConfigChangeLogsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterConfigChangeLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        param_change_logs: List[main_models.DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs] = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.db_cluster_id = db_cluster_id
        self.db_instance_id = db_instance_id
        # The instance ID.
        self.db_instance_name = db_instance_name
        # The parameter change logs.
        self.param_change_logs = param_change_logs
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.param_change_logs:
            for v1 in self.param_change_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        result['ParamChangeLogs'] = []
        if self.param_change_logs is not None:
            for k1 in self.param_change_logs:
                result['ParamChangeLogs'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        self.param_change_logs = []
        if m.get('ParamChangeLogs') is not None:
            for k1 in m.get('ParamChangeLogs'):
                temp_model = main_models.DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs()
                self.param_change_logs.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_applied: bool = None,
        name: str = None,
        new_value: str = None,
        old_value: str = None,
    ):
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # The ID of the change log.
        self.id = id
        # Indicates whether the modification has taken effect.
        self.is_applied = is_applied
        # The parameter name.
        self.name = name
        self.new_value = new_value
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_applied is not None:
            result['IsApplied'] = self.is_applied

        if self.name is not None:
            result['Name'] = self.name

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsApplied') is not None:
            self.is_applied = m.get('IsApplied')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        return self

