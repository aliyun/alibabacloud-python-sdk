# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CreateAppInstanceRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        auto_renew: bool = None,
        client_token: str = None,
        create_action: str = None,
        deploy_area: str = None,
        description: str = None,
        duration: int = None,
        extend: str = None,
        name: str = None,
        payment_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
        resource_group_id: str = None,
        site_version: str = None,
        tags: List[main_models.CreateAppInstanceRequestTags] = None,
        version: str = None,
    ):
        # Application type
        self.application_type = application_type
        # Whether to enable auto-renewal upon expiration
        self.auto_renew = auto_renew
        # Ensures idempotence of the request. Generate a unique value from your client to ensure that it is unique across different requests. ClientToken only supports ASCII characters and cannot exceed 64 characters
        self.client_token = client_token
        self.create_action = create_action
        # Deployment area
        self.deploy_area = deploy_area
        self.description = description
        # Required. The number of subscription periods
        self.duration = duration
        # Extended information
        self.extend = extend
        self.name = name
        # Payment type
        self.payment_type = payment_type
        # Required. The unit of the subscription period, Year: Year, Month: Month, Day: Day, Hour: Hour
        self.pricing_cycle = pricing_cycle
        # Required. The quantity of instances to be ordered.
        self.quantity = quantity
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Site version
        self.site_version = site_version
        # List of tags
        self.tags = tags
        self.version = version

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
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.create_action is not None:
            result['CreateAction'] = self.create_action

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateAction') is not None:
            self.create_action = m.get('CreateAction')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateAppInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateAppInstanceRequestTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # tag key
        self.tag_key = tag_key
        # value of tag 0
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

