# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceTypeRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        filter_read_only: bool = None,
        terraform_provider_version: str = None,
    ):
        self.accept_language = accept_language
        self.filter_read_only = filter_read_only
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language

        if self.filter_read_only is not None:
            result['filterReadOnly'] = self.filter_read_only

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')

        if m.get('filterReadOnly') is not None:
            self.filter_read_only = m.get('filterReadOnly')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        return self

