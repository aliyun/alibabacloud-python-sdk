# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationGroupRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        client_token: str = None,
        cms_group_id: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The ID of the region in which the related sources reside.
        # 
        # This parameter is required.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The key of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application name is used for this parameter by default.
        self.import_tag_key = import_tag_key
        # The value of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application group name is used for this parameter by default.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id

        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id

        if self.description is not None:
            result['Description'] = self.description

        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key

        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')

        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')

        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

