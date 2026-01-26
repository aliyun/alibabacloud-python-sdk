# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
        tags: List[main_models.UntagResourcesRequestTags] = None,
    ):
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKey.N parameter is not specified. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.all = all
        # The resource IDs. You can specify a maximum of 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the ARMS resources for which you want to modify tags. Valid values:
        # 
        # *   WEB: Browser Monitoring
        # *   APPLICATION: Application Monitoring
        # *   PROMETHEUS: Managed Service for Prometheus
        # *   SYNTHETICTASK: Synthetic Monitoring
        # *   ALERTRULE: Application Monitoring alert rule
        # *   PROMETHEUSALERTRULE: Managed Service for Prometheus alert rule
        # *   XTRACEAPP: Managed Service for OpenTelemetry
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys. You can specify a maximum of 20 tag keys.
        self.tag_key = tag_key
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UntagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UntagResourcesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

