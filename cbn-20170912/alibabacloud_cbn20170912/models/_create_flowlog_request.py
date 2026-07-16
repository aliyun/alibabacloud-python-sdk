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
        # Generate a value for this parameter from your client. Make sure that the value is unique for each request. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the flow log.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with \\`http\\://\\` or \\`https\\://\\`.
        self.description = description
        # The name of the flow log.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with \\`http\\://\\` or \\`https\\://\\`.
        self.flow_log_name = flow_log_name
        # The aggregation interval for the flow log. Unit: seconds. Valid values: **60** and **600**. Default value: **600**.
        self.interval = interval
        # A custom string of log fields for the flow log.
        # 
        # The format is defined as:
        # `${field 1}${field 2}${field 3}...${field n}`
        # 
        # - If you do not specify this parameter, all default fields are logged.
        # 
        # - If you specify this parameter, you must start the string with `${srcaddr}${dstaddr}${bytes}` because these are required parameters. For more information about all supported log fields, see [Configure a flow log](https://help.aliyun.com/document_detail/339822.html).
        self.log_format_string = log_format_string
        # The Logstore that is used to store the captured traffic.
        # 
        # - If you have already created a Logstore in the current region, enter the name of the Logstore.
        # 
        # - If you have not created a Logstore in the current region, you can specify a custom name for the Logstore. The system automatically creates the Logstore.
        #   The name of the Logstore must meet the following requirements:
        # 
        #   - The name must be unique within the same project.
        # 
        #   - It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        #   - It must start and end with a lowercase letter or a digit.
        # 
        #   - It must be 3 to 63 characters in length.
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The project that is used to store the captured traffic.
        # 
        # - If you have already created a project in the current region, enter the name of the project.
        # 
        # - If you have not created a project in the current region, you can specify a custom name for the project. The system automatically creates the project.
        # 
        #   A project name must be globally unique within an Alibaba Cloud region and cannot be modified after the project is created. The name must meet the following requirements:
        # 
        #   - The name must be globally unique.
        # 
        #   - It can contain only lowercase letters, digits, and hyphens (-).
        # 
        #   - It must start and end with a lowercase letter or a digit.
        # 
        #   - It must be 3 to 63 characters in length.
        self.project_name = project_name
        # The region ID of the flow log.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag.
        # 
        # You can add up to 20 tags in each call.
        self.tag = tag
        # The ID of the VPC connection, VPN connection, VBR connection, ECR connection, or inter-region connection.
        # 
        # If you want to configure a flow log for a transit router instance, do not specify this parameter.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the transit router instance.
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
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https:// `.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be an empty string or a string of up to 128 characters. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https:// `.
        # 
        # Each tag key must have a unique tag value. You can specify up to 20 tag values.
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

