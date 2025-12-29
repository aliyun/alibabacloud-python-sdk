# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationGroupResponseBody(DaraModel):
    def __init__(
        self,
        application_group: main_models.CreateApplicationGroupResponseBodyApplicationGroup = None,
        request_id: str = None,
    ):
        # The information about the application group.
        self.application_group = application_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = main_models.CreateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m.get('ApplicationGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateApplicationGroupResponseBodyApplicationGroup(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        cms_group_id: str = None,
        create_date: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        update_date: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The time when the application group was created.
        self.create_date = create_date
        # The ID of the region in which the related sources reside.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The key of the tag.
        self.import_tag_key = import_tag_key
        # The value of the tag.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The time when the application group was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

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

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

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

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

