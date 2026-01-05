# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetFunctionResponseBody(DaraModel):
    def __init__(
        self,
        function: main_models.GetFunctionResponseBodyFunction = None,
        request_id: str = None,
    ):
        # UDF function details
        self.function = function
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = main_models.GetFunctionResponseBodyFunction()
            self.function = temp_model.from_map(m.get('Function'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFunctionResponseBodyFunction(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The time when the UDF was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The unique identifier of the UDF function.
        # 
        # >  This field is of type Long in SDK versions prior to 8.0.0, and of type String in SDK version 8.0.0 and later. This change does not affect the normal use of the SDK; parameters are still returned according to the type defined in the SDK. Compilation failures due to the type change may occur only when upgrading the SDK across version 8.0.0, in which case users need to manually correct the data type.
        self.id = id
        # The time when the UDF was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the UDF.
        self.name = name
        # The owner of the UDF.
        self.owner = owner
        # The ID of the DataWorks workspace to which the UDF belongs.
        self.project_id = project_id
        # The FlowSpec field information about the UDF. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
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

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

