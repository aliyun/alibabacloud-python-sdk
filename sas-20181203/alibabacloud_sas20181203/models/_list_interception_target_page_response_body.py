# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListInterceptionTargetPageResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListInterceptionTargetPageResponseBodyPageInfo = None,
        request_id: str = None,
        rule_target_list: List[main_models.ListInterceptionTargetPageResponseBodyRuleTargetList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the network objects.
        self.rule_target_list = rule_target_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.rule_target_list:
            for v1 in self.rule_target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleTargetList'] = []
        if self.rule_target_list is not None:
            for k1 in self.rule_target_list:
                result['RuleTargetList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListInterceptionTargetPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_target_list = []
        if m.get('RuleTargetList') is not None:
            for k1 in m.get('RuleTargetList'):
                temp_model = main_models.ListInterceptionTargetPageResponseBodyRuleTargetList()
                self.rule_target_list.append(temp_model.from_map(k1))

        return self

class ListInterceptionTargetPageResponseBodyRuleTargetList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        image_list: List[str] = None,
        namespace: str = None,
        rule_type: str = None,
        tag_list: List[str] = None,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application of the network object.
        self.app_name = app_name
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The name of the container cluster.
        self.cluster_name = cluster_name
        # The images of the network object.
        self.image_list = image_list
        # The namespace to which the network object belongs.
        self.namespace = namespace
        # The type of the rule. Valid value:
        # 
        # *   customize: custom rule
        self.rule_type = rule_type
        # The tags specified for the network object.
        self.tag_list = tag_list
        # The ID of the network object.
        # 
        # > You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the IDs of network objects.
        self.target_id = target_id
        # The name of the network object.
        self.target_name = target_name
        # The type of the network object. Valid value:
        # 
        # *   IMAGE
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class ListInterceptionTargetPageResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

