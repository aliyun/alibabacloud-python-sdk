# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridProxyPolicyResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        policy_list: List[main_models.DescribeHybridProxyPolicyResponseBodyPolicyList] = None,
        request_id: str = None,
    ):
        # The number of entries on the current page.
        self.count = count
        # The data collection configurations of the proxy cluster.
        self.policy_list = policy_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_list:
            for v1 in self.policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.DescribeHybridProxyPolicyResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridProxyPolicyResponseBodyPolicyList(DaraModel):
    def __init__(
        self,
        info: List[main_models.DescribeHybridProxyPolicyResponseBodyPolicyListInfo] = None,
        policy_type: str = None,
    ):
        # The information about the policy.
        self.info = info
        # The type of the policy. Valid values:
        # 
        # *   **limitFrequency**
        # *   **limitBandWidth**
        self.policy_type = policy_type

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['Info'].append(k1.to_map() if k1 else None)

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k1 in m.get('Info'):
                temp_model = main_models.DescribeHybridProxyPolicyResponseBodyPolicyListInfo()
                self.info.append(temp_model.from_map(k1))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

class DescribeHybridProxyPolicyResponseBodyPolicyListInfo(DaraModel):
    def __init__(
        self,
        config: str = None,
        file_name: str = None,
        type: str = None,
    ):
        # The value of the policy configurations.
        self.config = config
        # The name of the file. After you configure a blocking policy, the blocked data is written to the file.
        self.file_name = file_name
        # The type of the policy that you configured. Valid values:
        # 
        # *   **file**
        # *   **net**
        # *   **process**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

