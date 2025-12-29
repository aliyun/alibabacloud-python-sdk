# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationGroupResponseBody(DaraModel):
    def __init__(
        self,
        application_group: main_models.UpdateApplicationGroupResponseBodyApplicationGroup = None,
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
            temp_model = main_models.UpdateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m.get('ApplicationGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateApplicationGroupResponseBodyApplicationGroup(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        created_date: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        updated_date: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The time when the application group was created.
        self.created_date = created_date
        # The ID of the region in which the related resources reside.
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
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

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

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

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

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

