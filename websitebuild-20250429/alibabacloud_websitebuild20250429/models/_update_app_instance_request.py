# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class UpdateAppInstanceRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        biz_id: str = None,
        client_token: str = None,
        deploy_area: str = None,
        description: str = None,
        extend: str = None,
        icon_url: str = None,
        name: str = None,
        payment_type: str = None,
        resource_group_id: str = None,
        site_version: str = None,
        tags: List[main_models.UpdateAppInstanceRequestTags] = None,
        thumbnail_url: str = None,
    ):
        # Application type
        self.application_type = application_type
        # Business ID
        self.biz_id = biz_id
        # Ensures the idempotence of the request. Generate a unique value from your client for this parameter to guarantee uniqueness across different requests. ClientToken supports only ASCII characters and must not exceed 64 characters.
        self.client_token = client_token
        # Deployment area
        self.deploy_area = deploy_area
        # Application description
        self.description = description
        # Extension information
        self.extend = extend
        # Application icon
        self.icon_url = icon_url
        # Application name
        self.name = name
        # Payment type
        self.payment_type = payment_type
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # Website version
        self.site_version = site_version
        # Tags.
        self.tags = tags
        # Application thumbnail
        self.thumbnail_url = thumbnail_url

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

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.description is not None:
            result['Description'] = self.description

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateAppInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        return self

class UpdateAppInstanceRequestTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the instance. Valid values for N: **1** to **20**. If you specify this parameter, it cannot be an empty string.
        # 
        # It can contain up to 64 characters, must not start with `aliyun` or `acs:`, and must not contain `http://` or `https://`.
        self.tag_key = tag_key
        # The tag value of the instance. Valid values for N: **1** to **20**. If you specify this parameter, it can be an empty string.
        # 
        # It can contain up to 128 characters, must not start with `aliyun` or `acs:`, and must not contain `http://` or `https://`.
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

