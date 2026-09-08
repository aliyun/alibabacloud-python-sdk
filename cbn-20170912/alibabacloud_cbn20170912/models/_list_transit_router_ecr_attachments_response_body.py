# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterEcrAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_attachments: List[main_models.ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachments] = None,
    ):
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # The token for the next paged query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of ECR connection information.
        self.transit_router_attachments = transit_router_attachments

    def validate(self):
        if self.transit_router_attachments:
            for v1 in self.transit_router_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k1 in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k1 in m.get('TransitRouterAttachments'):
                temp_model = main_models.ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k1))

        return self

class ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachments(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        cen_id: str = None,
        creation_time: str = None,
        ecr_id: str = None,
        ecr_owner_id: int = None,
        order_type: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachmentsTags] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
        transit_router_region_id: str = None,
    ):
        # Indicates whether the Enterprise Edition transit router automatically publishes route entries to the ECR instance.
        # 
        # The value is **true** only, which indicates that route entries are automatically published.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The CEN instance ID.
        self.cen_id = cen_id
        # The time when the ECR connection was created.
        # 
        # The time is displayed in the ISO 8601 standard in UTC. Format: YYYY-MM-DDThh:mmZ.
        self.creation_time = creation_time
        # The instance ID of the associated Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account to which the ECR instance belongs.
        self.ecr_owner_id = ecr_owner_id
        # The payer of the network instance. Valid values:
        # 
        # - **PayByCenOwner**: The connection fee and data processing fee of the ECR instance are paid by the account that owns the transit router instance.
        # - **PayByResourceOwner**: The connection fee and data processing fee of the ECR instance are paid by the account that owns the ECR instance.
        self.order_type = order_type
        # The resource type of the connection.
        # 
        # The value is **ECR** only, which indicates an Express Connect Router (ECR) instance.
        self.resource_type = resource_type
        # The status of the ECR connection.
        # 
        # - **Attached**: attached.
        # - **Attaching**: being attached.
        # - **Detaching**: being detached.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The description of the ECR connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ECR connection ID.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the ECR connection.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The Enterprise Edition transit router instance ID.
        self.transit_router_id = transit_router_id
        # The region ID of the transit router.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the region information corresponding to the region ID.
        self.transit_router_region_id = transit_router_region_id

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
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.ecr_owner_id is not None:
            result['EcrOwnerId'] = self.ecr_owner_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_region_id is not None:
            result['TransitRouterRegionId'] = self.transit_router_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('EcrOwnerId') is not None:
            self.ecr_owner_id = m.get('EcrOwnerId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterRegionId') is not None:
            self.transit_router_region_id = m.get('TransitRouterRegionId')

        return self

class ListTransitRouterEcrAttachmentsResponseBodyTransitRouterAttachmentsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

