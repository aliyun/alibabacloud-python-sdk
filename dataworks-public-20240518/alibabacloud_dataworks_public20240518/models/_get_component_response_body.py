# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetComponentResponseBody(DaraModel):
    def __init__(
        self,
        component: main_models.GetComponentResponseBodyComponent = None,
        request_id: str = None,
    ):
        # JSON serialization of the component module.
        self.component = component
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.component:
            self.component.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component is not None:
            result['Component'] = self.component.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Component') is not None:
            temp_model = main_models.GetComponentResponseBodyComponent()
            self.component = temp_model.from_map(m.get('Component'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetComponentResponseBodyComponent(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        region_id: str = None,
        spec: str = None,
    ):
        # The ID of the dataset acceleration component. For information on how to obtain the component ID, see [ListComponents](https://help.aliyun.com/document_detail/2979566.html).
        self.component_id = component_id
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.create_time = create_time
        # The description.
        self.description = description
        # The modification time (millisecond-level timestamp).
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.modify_time = modify_time
        # Parameter
        self.name = name
        # The ID of the task owner.
        self.owner = owner
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The region ID, such as ap-southeast-1. The region ID is automatically parsed from your endpoint.
        self.region_id = region_id
        # The FlowSpec information for this workflow. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow/).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

