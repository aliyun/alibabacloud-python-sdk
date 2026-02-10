# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListContainerDefenseRuleClustersResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: List[main_models.ListContainerDefenseRuleClustersResponseBodyClusterList] = None,
        code: str = None,
        count: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The clusters.
        self.cluster_list = cluster_list
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The total number of entries returned.
        self.count = count
        # The HTTP status code that is returned.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.cluster_list:
            for v1 in self.cluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterList'] = []
        if self.cluster_list is not None:
            for k1 in self.cluster_list:
                result['ClusterList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_list = []
        if m.get('ClusterList') is not None:
            for k1 in m.get('ClusterList'):
                temp_model = main_models.ListContainerDefenseRuleClustersResponseBodyClusterList()
                self.cluster_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListContainerDefenseRuleClustersResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        all_namespace: int = None,
        cluster_id: str = None,
        namespaces: List[str] = None,
        rule_id: int = None,
    ):
        # Indicates whether all namespaces are included. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.all_namespace = all_namespace
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The namespaces.
        self.namespaces = namespaces
        # The ID of the rule.
        # 
        # >  You can call the [ListInterceptionRulePage](https://help.aliyun.com/document_detail/2590599.html) operation to query the IDs of rules.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_namespace is not None:
            result['AllNamespace'] = self.all_namespace

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllNamespace') is not None:
            self.all_namespace = m.get('AllNamespace')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

