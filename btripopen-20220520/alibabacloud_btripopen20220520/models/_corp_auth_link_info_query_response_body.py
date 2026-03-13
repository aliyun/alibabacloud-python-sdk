# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CorpAuthLinkInfoQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.CorpAuthLinkInfoQueryResponseBodyModule = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.CorpAuthLinkInfoQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CorpAuthLinkInfoQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        link_corps: List[main_models.CorpAuthLinkInfoQueryResponseBodyModuleLinkCorps] = None,
        org_corp: main_models.CorpAuthLinkInfoQueryResponseBodyModuleOrgCorp = None,
    ):
        self.link_corps = link_corps
        self.org_corp = org_corp

    def validate(self):
        if self.link_corps:
            for v1 in self.link_corps:
                 if v1:
                    v1.validate()
        if self.org_corp:
            self.org_corp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['link_corps'] = []
        if self.link_corps is not None:
            for k1 in self.link_corps:
                result['link_corps'].append(k1.to_map() if k1 else None)

        if self.org_corp is not None:
            result['org_corp'] = self.org_corp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.link_corps = []
        if m.get('link_corps') is not None:
            for k1 in m.get('link_corps'):
                temp_model = main_models.CorpAuthLinkInfoQueryResponseBodyModuleLinkCorps()
                self.link_corps.append(temp_model.from_map(k1))

        if m.get('org_corp') is not None:
            temp_model = main_models.CorpAuthLinkInfoQueryResponseBodyModuleOrgCorp()
            self.org_corp = temp_model.from_map(m.get('org_corp'))

        return self

class CorpAuthLinkInfoQueryResponseBodyModuleOrgCorp(DaraModel):
    def __init__(
        self,
        corp_name: str = None,
        open_corp_id: str = None,
        true_corp_id: str = None,
    ):
        self.corp_name = corp_name
        self.open_corp_id = open_corp_id
        self.true_corp_id = true_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.open_corp_id is not None:
            result['open_corp_id'] = self.open_corp_id

        if self.true_corp_id is not None:
            result['true_corp_id'] = self.true_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('open_corp_id') is not None:
            self.open_corp_id = m.get('open_corp_id')

        if m.get('true_corp_id') is not None:
            self.true_corp_id = m.get('true_corp_id')

        return self

class CorpAuthLinkInfoQueryResponseBodyModuleLinkCorps(DaraModel):
    def __init__(
        self,
        corp_name: str = None,
        open_corp_id: str = None,
        true_corp_id: str = None,
    ):
        self.corp_name = corp_name
        self.open_corp_id = open_corp_id
        self.true_corp_id = true_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.open_corp_id is not None:
            result['open_corp_id'] = self.open_corp_id

        if self.true_corp_id is not None:
            result['true_corp_id'] = self.true_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('open_corp_id') is not None:
            self.open_corp_id = m.get('open_corp_id')

        if m.get('true_corp_id') is not None:
            self.true_corp_id = m.get('true_corp_id')

        return self

