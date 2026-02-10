# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetInterceptionTargetDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_target: main_models.GetInterceptionTargetDetailResponseBodyRuleTarget = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the network object.
        self.rule_target = rule_target

    def validate(self):
        if self.rule_target:
            self.rule_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_target is not None:
            result['RuleTarget'] = self.rule_target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleTarget') is not None:
            temp_model = main_models.GetInterceptionTargetDetailResponseBodyRuleTarget()
            self.rule_target = temp_model.from_map(m.get('RuleTarget'))

        return self

class GetInterceptionTargetDetailResponseBodyRuleTarget(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        image_list: List[str] = None,
        namespace: str = None,
        tag_list: List[str] = None,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application to which the network object belongs.
        self.app_name = app_name
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The name of the container cluster.
        self.cluster_name = cluster_name
        # An array that consists of the images of the network object.
        self.image_list = image_list
        # The namespace.
        self.namespace = namespace
        # An array that consists of the labels specified for the network object.
        self.tag_list = tag_list
        # The ID of the network object.
        self.target_id = target_id
        # The name of the network object.
        self.target_name = target_name
        # The type of the network object. Valid values:
        # 
        # *   **IMAGE**: image
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

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

