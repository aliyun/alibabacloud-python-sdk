# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetSasContainerWebDefenseRuleApplicationResponseBody(DaraModel):
    def __init__(
        self,
        container_web_defense_app_list: List[main_models.GetSasContainerWebDefenseRuleApplicationResponseBodyContainerWebDefenseAppList] = None,
        request_id: str = None,
    ):
        # The applications.
        self.container_web_defense_app_list = container_web_defense_app_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.container_web_defense_app_list:
            for v1 in self.container_web_defense_app_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerWebDefenseAppList'] = []
        if self.container_web_defense_app_list is not None:
            for k1 in self.container_web_defense_app_list:
                result['ContainerWebDefenseAppList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_web_defense_app_list = []
        if m.get('ContainerWebDefenseAppList') is not None:
            for k1 in m.get('ContainerWebDefenseAppList'):
                temp_model = main_models.GetSasContainerWebDefenseRuleApplicationResponseBodyContainerWebDefenseAppList()
                self.container_web_defense_app_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSasContainerWebDefenseRuleApplicationResponseBodyContainerWebDefenseAppList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        cluster_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        rule_id: int = None,
        tag: str = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The ID of the container cluster.
        # 
        # >  The IDs of clusters can be obtained by using the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/182997.html) operation.
        self.cluster_id = cluster_id
        # The time when the application was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The last modification time. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the node.
        self.id = id
        # The ID of the rule.
        self.rule_id = rule_id
        # The value of the application label.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

