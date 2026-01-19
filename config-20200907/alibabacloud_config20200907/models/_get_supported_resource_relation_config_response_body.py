# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetSupportedResourceRelationConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_relation_config_list: List[main_models.GetSupportedResourceRelationConfigResponseBodyResourceRelationConfigList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # An array that contains the relationships.
        self.resource_relation_config_list = resource_relation_config_list

    def validate(self):
        if self.resource_relation_config_list:
            for v1 in self.resource_relation_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceRelationConfigList'] = []
        if self.resource_relation_config_list is not None:
            for k1 in self.resource_relation_config_list:
                result['ResourceRelationConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_relation_config_list = []
        if m.get('ResourceRelationConfigList') is not None:
            for k1 in m.get('ResourceRelationConfigList'):
                temp_model = main_models.GetSupportedResourceRelationConfigResponseBodyResourceRelationConfigList()
                self.resource_relation_config_list.append(temp_model.from_map(k1))

        return self

class GetSupportedResourceRelationConfigResponseBodyResourceRelationConfigList(DaraModel):
    def __init__(
        self,
        relation_type: str = None,
        target_resource_type: str = None,
    ):
        # The type of the relationship between the resource and the object. Valid values:
        # 
        # *   IsContained: The object is included as part of the resource.
        # *   IsAttachedTo: The object is added to the resource.
        # *   IsAssociatedIn: The object is associated with the resource.
        # *   Contains: The actual value contains the expected value.
        self.relation_type = relation_type
        # The resource type.
        self.target_resource_type = target_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.target_resource_type is not None:
            result['TargetResourceType'] = self.target_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('TargetResourceType') is not None:
            self.target_resource_type = m.get('TargetResourceType')

        return self

