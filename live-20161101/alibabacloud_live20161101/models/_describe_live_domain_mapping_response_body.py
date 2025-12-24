# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainMappingResponseBody(DaraModel):
    def __init__(
        self,
        live_domain_models: main_models.DescribeLiveDomainMappingResponseBodyLiveDomainModels = None,
        request_id: str = None,
    ):
        # The mappings of the queried domain name.
        self.live_domain_models = live_domain_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_domain_models:
            self.live_domain_models.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_domain_models is not None:
            result['LiveDomainModels'] = self.live_domain_models.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveDomainModels') is not None:
            temp_model = main_models.DescribeLiveDomainMappingResponseBodyLiveDomainModels()
            self.live_domain_models = temp_model.from_map(m.get('LiveDomainModels'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainMappingResponseBodyLiveDomainModels(DaraModel):
    def __init__(
        self,
        live_domain_model: List[main_models.DescribeLiveDomainMappingResponseBodyLiveDomainModelsLiveDomainModel] = None,
    ):
        self.live_domain_model = live_domain_model

    def validate(self):
        if self.live_domain_model:
            for v1 in self.live_domain_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveDomainModel'] = []
        if self.live_domain_model is not None:
            for k1 in self.live_domain_model:
                result['LiveDomainModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_domain_model = []
        if m.get('LiveDomainModel') is not None:
            for k1 in m.get('LiveDomainModel'):
                temp_model = main_models.DescribeLiveDomainMappingResponseBodyLiveDomainModelsLiveDomainModel()
                self.live_domain_model.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainMappingResponseBodyLiveDomainModelsLiveDomainModel(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        type: str = None,
    ):
        # The domain name to which the queried domain name is mapped.
        self.domain_name = domain_name
        # The type of the queried domain name. Valid values:
        # 
        # *   **vhost**: main streaming domain
        # *   **publish**: ingest domain
        # *   **play**: sub-streaming domain
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

