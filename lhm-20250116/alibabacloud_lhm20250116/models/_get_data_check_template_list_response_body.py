# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetDataCheckTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetDataCheckTemplateListResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data list returned by the operation. For the structure of each element, see the child field descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed. Check errCode and errMessage for details.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetDataCheckTemplateListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDataCheckTemplateListResponseBodyData(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        check_type_export: str = None,
        check_type_name: int = None,
        ds_types: str = None,
        engine_types: str = None,
        gmt_modified: str = None,
        is_builtin: int = None,
        is_used_by_task: bool = None,
        template_desc: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The validation rule type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # - 3: custom comparison.
        # - 4: full-text comparison.
        # - 5: null rate comparison.
        self.check_type = check_type
        # The display name of the check type, used in exported reports.
        self.check_type_export = check_type_export
        # The name of the check type.
        self.check_type_name = check_type_name
        # The list of covered data source types. Multiple values are separated by commas.
        self.ds_types = ds_types
        # The list of covered validation engine types, such as Tez and MapReduce. When returned as a string, multiple values are separated by commas.
        self.engine_types = engine_types
        # The modification time.
        self.gmt_modified = gmt_modified
        # Specifies whether the template is built-in. Valid values:
        # - 0: No. The template is a custom template.
        # - 1: Yes. The template is a built-in template.
        self.is_builtin = is_builtin
        # Indicates whether the template is referenced by a validation task. Valid values:
        # - true: The template is referenced.
        # - false: The template is not referenced.
        # The delete operation does not verify this reference relationship. Confirm before deleting.
        self.is_used_by_task = is_used_by_task
        # The template description.
        self.template_desc = template_desc
        # The validation template ID (logical foreign key) that uniquely identifies a validation template.
        self.template_id = template_id
        # The name of the validation template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.check_type_export is not None:
            result['checkTypeExport'] = self.check_type_export

        if self.check_type_name is not None:
            result['checkTypeName'] = self.check_type_name

        if self.ds_types is not None:
            result['dsTypes'] = self.ds_types

        if self.engine_types is not None:
            result['engineTypes'] = self.engine_types

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_builtin is not None:
            result['isBuiltin'] = self.is_builtin

        if self.is_used_by_task is not None:
            result['isUsedByTask'] = self.is_used_by_task

        if self.template_desc is not None:
            result['templateDesc'] = self.template_desc

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('checkTypeExport') is not None:
            self.check_type_export = m.get('checkTypeExport')

        if m.get('checkTypeName') is not None:
            self.check_type_name = m.get('checkTypeName')

        if m.get('dsTypes') is not None:
            self.ds_types = m.get('dsTypes')

        if m.get('engineTypes') is not None:
            self.engine_types = m.get('engineTypes')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isBuiltin') is not None:
            self.is_builtin = m.get('isBuiltin')

        if m.get('isUsedByTask') is not None:
            self.is_used_by_task = m.get('isUsedByTask')

        if m.get('templateDesc') is not None:
            self.template_desc = m.get('templateDesc')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

