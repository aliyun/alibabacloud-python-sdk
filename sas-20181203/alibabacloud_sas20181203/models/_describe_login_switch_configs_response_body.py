# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeLoginSwitchConfigsResponseBody(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.DescribeLoginSwitchConfigsResponseBodyConfigList] = None,
        count: int = None,
        request_id: str = None,
    ):
        # The configuration item returned.
        self.config_list = config_list
        # The number of returned configuration items.
        self.count = count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeLoginSwitchConfigsResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLoginSwitchConfigsResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        item: str = None,
        status: int = None,
    ):
        # The type of the alert that you enabled or disabled. Valid values:
        # 
        # *   **login_common_ip**: alerts for unapproved logon IP addresses
        # *   **login_common_time**: alerts for unapproved logon time ranges
        # *   **login_common_account**: alerts for unapproved logon accounts
        self.item = item
        # The status of the Log Service feature. Valid values:
        # 
        # *   **0**: The feature is disabled.
        # *   **1**: The feature is enabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

