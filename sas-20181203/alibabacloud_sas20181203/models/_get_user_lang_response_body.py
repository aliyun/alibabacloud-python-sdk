# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetUserLangResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sas_user_lang: main_models.GetUserLangResponseBodySasUserLang = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The language settings.
        self.sas_user_lang = sas_user_lang

    def validate(self):
        if self.sas_user_lang:
            self.sas_user_lang.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sas_user_lang is not None:
            result['SasUserLang'] = self.sas_user_lang.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SasUserLang') is not None:
            temp_model = main_models.GetUserLangResponseBodySasUserLang()
            self.sas_user_lang = temp_model.from_map(m.get('SasUserLang'))

        return self

class GetUserLangResponseBodySasUserLang(DaraModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language specified for log analysis. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

