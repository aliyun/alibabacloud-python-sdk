# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DataModuleMapListSpnTypeMapListValue(DaraModel):
    def __init__(
        self,
        filter_modules: List[main_models.DataModuleMapListSpnTypeMapListValueFilterModules] = None,
        show_modules: List[main_models.DataModuleMapListSpnTypeMapListValueShowModules] = None,
    ):
        self.filter_modules = filter_modules
        self.show_modules = show_modules

    def validate(self):
        if self.filter_modules:
            for v1 in self.filter_modules:
                 if v1:
                    v1.validate()
        if self.show_modules:
            for v1 in self.show_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k1 in self.filter_modules:
                result['FilterModules'].append(k1.to_map() if k1 else None)

        result['ShowModules'] = []
        if self.show_modules is not None:
            for k1 in self.show_modules:
                result['ShowModules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k1 in m.get('FilterModules'):
                temp_model = main_models.DataModuleMapListSpnTypeMapListValueFilterModules()
                self.filter_modules.append(temp_model.from_map(k1))

        self.show_modules = []
        if m.get('ShowModules') is not None:
            for k1 in m.get('ShowModules'):
                temp_model = main_models.DataModuleMapListSpnTypeMapListValueShowModules()
                self.show_modules.append(temp_model.from_map(k1))

        return self

class DataModuleMapListSpnTypeMapListValueShowModules(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        module_code: str = None,
        module_name: str = None,
    ):
        self.module_id = module_id
        self.module_code = module_code
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class DataModuleMapListSpnTypeMapListValueFilterModules(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        module_code: str = None,
        module_name: str = None,
    ):
        self.module_id = module_id
        self.module_code = module_code
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

