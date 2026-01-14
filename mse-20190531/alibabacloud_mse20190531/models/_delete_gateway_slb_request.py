# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGatewaySlbRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        delete_slb: bool = None,
        gateway_unique_id: str = None,
        id: str = None,
        slb_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to delete the SLB instance purchased for the gateway when you delete the gateway.
        self.delete_slb = delete_slb
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the association record.
        self.id = id
        # The ID of the SLB instance that needs to be deleted.
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.delete_slb is not None:
            result['DeleteSlb'] = self.delete_slb

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DeleteSlb') is not None:
            self.delete_slb = m.get('DeleteSlb')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        return self

