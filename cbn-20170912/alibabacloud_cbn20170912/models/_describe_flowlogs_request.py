# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowlogsRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        client_token: str = None,
        description: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        flow_log_version: str = None,
        interval: int = None,
        log_store_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[main_models.DescribeFlowlogsRequestTag] = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among all requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId for each API request may be different.
        self.client_token = client_token
        # The description of the flow log.
        # 
        # The description is optional. If you enter a description, it must be 1 to 256 characters in length, and cannot start with http:// or https://.
        self.description = description
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The name of the flow log.
        # 
        # The name is optional. If you enter a name, it must be 1 to 128 characters in length, and cannot start with http:// or https://.
        self.flow_log_name = flow_log_name
        # The flow log version.
        # 
        # Flow logs are automatically created in the latest version, which is **3**.
        self.flow_log_version = flow_log_version
        # The time window for collecting log data. Unit: seconds Valid values: **60** or **600** Default value: **600**.
        self.interval = interval
        # The name of the Logstore where the flow log is stored.
        # 
        # The name must be 3 to 63 characters in length, and can contain lowercase letters, digits, underscores (_), and hyphens (-). It must start or end with a lowercase letter or a digit.
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Minimum value: **1**. Default value: **20**.
        self.page_size = page_size
        # The name of the project where the flow log is stored.
        # 
        # The name must be 3 to 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). It must start or end with a lowercase letter or a digit.
        self.project_name = project_name
        # The ID of the region where the flow log is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the flow log. Valid values:
        # 
        # *   **Active**: The flow log is enabled.
        # *   **Inactive**: The flow log is disabled.
        self.status = status
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.flow_log_version is not None:
            result['FlowLogVersion'] = self.flow_log_version

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('FlowLogVersion') is not None:
            self.flow_log_version = m.get('FlowLogVersion')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFlowlogsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeFlowlogsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be 0 to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.
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

