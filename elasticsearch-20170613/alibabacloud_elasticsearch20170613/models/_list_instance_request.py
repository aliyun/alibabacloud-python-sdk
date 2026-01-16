# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        es_version: str = None,
        instance_category: str = None,
        instance_id: str = None,
        page: int = None,
        payment_type: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
        tags: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # cn-hangzhou-i
        self.description = description
        # advanced
        self.es_version = es_version
        # The number of data nodes.
        self.instance_category = instance_category
        # postpaid
        self.instance_id = instance_id
        # [{"tagKey":"key1","tagValue":"value1"}]
        self.page = page
        # Specifies whether to include dedicated master nodes. Valid values:
        # 
        # *   true: The files contain data that is dumped to the IA storage medium.
        # *   false: The files do not contain data that is dumped to the IA storage medium.
        self.payment_type = payment_type
        # The ID of the request.
        self.resource_group_id = resource_group_id
        # vpc-bp16k1dvzxtmagcva\\*\\*\\*\\*
        self.size = size
        self.status = status
        # The header of the response.
        self.tags = tags
        # The number of entries returned per page.
        self.vpc_id = vpc_id
        # The returned data.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.page is not None:
            result['page'] = self.page

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['size'] = self.size

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

