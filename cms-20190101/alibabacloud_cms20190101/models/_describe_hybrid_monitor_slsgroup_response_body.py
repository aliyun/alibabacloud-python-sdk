# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridMonitorSLSGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        list: List[main_models.DescribeHybridMonitorSLSGroupResponseBodyList] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The queried Logstore groups.
        self.list = list
        # The error message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeHybridMonitorSLSGroupResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeHybridMonitorSLSGroupResponseBodyList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        slsgroup_config: List[main_models.DescribeHybridMonitorSLSGroupResponseBodyListSLSGroupConfig] = None,
        slsgroup_description: str = None,
        slsgroup_name: str = None,
        update_time: str = None,
    ):
        # The time when the Logstore group was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The configurations of the Logstore group.
        self.slsgroup_config = slsgroup_config
        # The description of the Logstore group.
        self.slsgroup_description = slsgroup_description
        # The name of the Logstore group.
        self.slsgroup_name = slsgroup_name
        # The time when the Logstore group was modified.
        # 
        # Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.slsgroup_config:
            for v1 in self.slsgroup_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['SLSGroupConfig'] = []
        if self.slsgroup_config is not None:
            for k1 in self.slsgroup_config:
                result['SLSGroupConfig'].append(k1.to_map() if k1 else None)

        if self.slsgroup_description is not None:
            result['SLSGroupDescription'] = self.slsgroup_description

        if self.slsgroup_name is not None:
            result['SLSGroupName'] = self.slsgroup_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.slsgroup_config = []
        if m.get('SLSGroupConfig') is not None:
            for k1 in m.get('SLSGroupConfig'):
                temp_model = main_models.DescribeHybridMonitorSLSGroupResponseBodyListSLSGroupConfig()
                self.slsgroup_config.append(temp_model.from_map(k1))

        if m.get('SLSGroupDescription') is not None:
            self.slsgroup_description = m.get('SLSGroupDescription')

        if m.get('SLSGroupName') is not None:
            self.slsgroup_name = m.get('SLSGroupName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeHybridMonitorSLSGroupResponseBodyListSLSGroupConfig(DaraModel):
    def __init__(
        self,
        slslogstore: str = None,
        slsproject: str = None,
        slsregion: str = None,
        slsuser_id: str = None,
    ):
        # The Logstore.
        self.slslogstore = slslogstore
        # The Simple Log Service project.
        self.slsproject = slsproject
        # The region ID.
        self.slsregion = slsregion
        # The member ID.
        # 
        # **Description** This parameter is returned when you call the operation by using an administrative account.
        self.slsuser_id = slsuser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slslogstore is not None:
            result['SLSLogstore'] = self.slslogstore

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion

        if self.slsuser_id is not None:
            result['SLSUserId'] = self.slsuser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogstore') is not None:
            self.slslogstore = m.get('SLSLogstore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')

        if m.get('SLSUserId') is not None:
            self.slsuser_id = m.get('SLSUserId')

        return self

