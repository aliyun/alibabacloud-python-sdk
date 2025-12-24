# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeClassicLinkInstancesResponseBody(DaraModel):
    def __init__(
        self,
        links: main_models.DescribeClassicLinkInstancesResponseBodyLinks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the ClassicLink connections between the instances reside in the classic network and VPCs.
        self.links = links
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of ClassicLink connections.
        self.total_count = total_count

    def validate(self):
        if self.links:
            self.links.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.links is not None:
            result['Links'] = self.links.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Links') is not None:
            temp_model = main_models.DescribeClassicLinkInstancesResponseBodyLinks()
            self.links = temp_model.from_map(m.get('Links'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeClassicLinkInstancesResponseBodyLinks(DaraModel):
    def __init__(
        self,
        link: List[main_models.DescribeClassicLinkInstancesResponseBodyLinksLink] = None,
    ):
        self.link = link

    def validate(self):
        if self.link:
            for v1 in self.link:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Link'] = []
        if self.link is not None:
            for k1 in self.link:
                result['Link'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.link = []
        if m.get('Link') is not None:
            for k1 in m.get('Link'):
                temp_model = main_models.DescribeClassicLinkInstancesResponseBodyLinksLink()
                self.link.append(temp_model.from_map(k1))

        return self

class DescribeClassicLinkInstancesResponseBodyLinksLink(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        vpc_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

