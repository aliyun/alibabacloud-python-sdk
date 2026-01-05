# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_template: main_models.GetDataQualityTemplateResponseBodyDataQualityTemplate = None,
        request_id: str = None,
    ):
        # The data quality rule template.
        self.data_quality_template = data_quality_template
        # The API request ID, which is generated as a UUID.
        self.request_id = request_id

    def validate(self):
        if self.data_quality_template:
            self.data_quality_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_template is not None:
            result['DataQualityTemplate'] = self.data_quality_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityTemplate') is not None:
            temp_model = main_models.GetDataQualityTemplateResponseBodyDataQualityTemplate()
            self.data_quality_template = temp_model.from_map(m.get('DataQualityTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityTemplateResponseBodyDataQualityTemplate(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        id: str = None,
        modify_time: int = None,
        modify_user: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The time when the data quality rule template was created.
        self.create_time = create_time
        # The creator of the data quality rule template.
        self.create_user = create_user
        # The ID of the data quality rule template.
        self.id = id
        # The time when the data quality rule template was updated.
        self.modify_time = modify_time
        # The last updater of the data quality rule template.
        self.modify_user = modify_user
        # The owner of the data quality rule template.
        self.owner = owner
        # The project ID.
        self.project_id = project_id
        # Specific configurations of the data quality rule template. For more information, see [Data quality Spec configuration description](~2963394~).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

