# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListClusterInterceptionConfigResponseBody(DaraModel):
    def __init__(
        self,
        cluster_config_list: List[main_models.ListClusterInterceptionConfigResponseBodyClusterConfigList] = None,
        page_info: main_models.ListClusterInterceptionConfigResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the configurations of the cluster.
        self.cluster_config_list = cluster_config_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cluster_config_list:
            for v1 in self.cluster_config_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterConfigList'] = []
        if self.cluster_config_list is not None:
            for k1 in self.cluster_config_list:
                result['ClusterConfigList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_config_list = []
        if m.get('ClusterConfigList') is not None:
            for k1 in m.get('ClusterConfigList'):
                temp_model = main_models.ListClusterInterceptionConfigResponseBodyClusterConfigList()
                self.cluster_config_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListClusterInterceptionConfigResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterInterceptionConfigResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        currrent_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.currrent_page = currrent_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.currrent_page is not None:
            result['CurrrentPage'] = self.currrent_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrrentPage') is not None:
            self.currrent_page = m.get('CurrrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListClusterInterceptionConfigResponseBodyClusterConfigList(DaraModel):
    def __init__(
        self,
        cluster_cnnfstatus: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        interception_switch: int = None,
        open_rule_count: int = None,
        support_cnnf: bool = None,
        total_rule_count: int = None,
    ):
        # The status of the container firewall feature. Valid values:
        # 
        # *   **-1**: unknown
        # *   **0**: abnormal
        # *   **1**: normal
        # *   **2**: normal to be confirmed
        self.cluster_cnnfstatus = cluster_cnnfstatus
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # *   **ManagedKubernetes**: managed Kubernetes cluster
        # *   **NotManagedKubernetes**: non-managed Kubernetes cluster
        # *   **PrivateKubernetes**: private cluster
        # *   **kubernetes**: dedicated Kubernetes cluster
        # *   **ask**: dedicated serverless Kubernetes (ASK) cluster
        self.cluster_type = cluster_type
        # The status of the defense rule. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.interception_switch = interception_switch
        # The number of defense rules that are in effect.
        self.open_rule_count = open_rule_count
        # Indicates whether the container firewall feature is supported.
        self.support_cnnf = support_cnnf
        # The total number of defense rules.
        self.total_rule_count = total_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_cnnfstatus is not None:
            result['ClusterCNNFStatus'] = self.cluster_cnnfstatus

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.interception_switch is not None:
            result['InterceptionSwitch'] = self.interception_switch

        if self.open_rule_count is not None:
            result['OpenRuleCount'] = self.open_rule_count

        if self.support_cnnf is not None:
            result['SupportCNNF'] = self.support_cnnf

        if self.total_rule_count is not None:
            result['TotalRuleCount'] = self.total_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCNNFStatus') is not None:
            self.cluster_cnnfstatus = m.get('ClusterCNNFStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('InterceptionSwitch') is not None:
            self.interception_switch = m.get('InterceptionSwitch')

        if m.get('OpenRuleCount') is not None:
            self.open_rule_count = m.get('OpenRuleCount')

        if m.get('SupportCNNF') is not None:
            self.support_cnnf = m.get('SupportCNNF')

        if m.get('TotalRuleCount') is not None:
            self.total_rule_count = m.get('TotalRuleCount')

        return self

