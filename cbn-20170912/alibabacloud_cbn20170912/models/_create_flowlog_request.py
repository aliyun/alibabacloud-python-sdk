# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateFlowlogRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        client_token: str = None,
        description: str = None,
        flow_log_name: str = None,
        interval: int = None,
        log_format_string: str = None,
        log_store_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        project_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateFlowlogRequestTag] = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the CEN instance.
        # 
        # This parameter is required.
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
        # The flow log name.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.flow_log_name = flow_log_name
        # The time window for collecting log data. Unit: seconds. Valid values: **60** and **600**. Default value: **600**.
        self.interval = interval
        # The strings that define the fields in the flow log.
        # 
        # Format: `${Field 1}${Field 2}${Field 3}...{Field n}`
        # 
        # *   If you do not configure this parameter, all fields are included in the flow log.
        # *   If you configure this parameter, start the string with `${srcaddr}${dstaddr}${bytes}` because `${srcaddr}${dstaddr}${bytes}` are required variables. For more information about the fields supported by flow logs, see [Configure a flow log](https://help.aliyun.com/document_detail/339822.html).
        self.log_format_string = log_format_string
        # The Logstore that stores the captured traffic data.
        # 
        # *   If a Logstore is already created in the selected region, enter the name of the Logstore.
        # 
        # *   If no Logstores are created in the selected region, enter a name and the system automatically creates a Logstore. The name of the Logstore. The name must meet the following requirements:
        # 
        #     *   The name must be unique in a project.
        #     *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        #     *   The name must start and end with a lowercase letter or a digit.
        #     *   The name must be 3 to 63 characters in length,
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The project that stores the captured traffic data.
        # 
        # *   If a project is already created in the selected region, enter the name of the project.
        # 
        # *   If no projects are created in the selected region, enter a name and the system automatically creates a project.
        # 
        #     The project name must be unique in a region. You cannot change the name after the project is created. The name must meet the following requirements:
        # 
        #     *   The name must be globally unique.
        #     *   The name can contain only lowercase letters, digits, and hyphens (-).
        #     *   The name must start and end with a lowercase letter or a digit.
        #     *   The name must be 3 to 63 characters in length,
        self.project_name = project_name
        # The ID of the region where the flow log is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        # 
        # You can specify at most 20 tags.
        self.tag = tag
        # The ID of the VPC connection, VPN connection, VBR connection, ECR connection, or inter-region connection.
        # 
        # If you create the flow log for a transfer router, skip this parameter.
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

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_format_string is not None:
            result['LogFormatString'] = self.log_format_string

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogFormatString') is not None:
            self.log_format_string = m.get('LogFormatString')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFlowlogRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class CreateFlowlogRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys.
        # 
        # The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length. The tag keys cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys in each call.
        self.key = key
        # The tag values.
        # 
        # The tag values can be an empty string or up to 128 characters in length. The tag values cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each key-value must be unique. You can specify at most 20 tag values in each call.
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

