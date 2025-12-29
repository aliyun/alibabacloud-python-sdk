# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        internet: str = None,
        internet_slb_charge_type: str = None,
        internet_slb_id: str = None,
        intranet: str = None,
        intranet_slb_charge_type: str = None,
        intranet_slb_id: str = None,
    ):
        # 0099b7be-5f5b-4512-a7fc-56049ef1\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.app_id = app_id
        # [{"port":80,"targetPort":8080,"protocol":"TCP"}]
        self.internet = internet
        # The billing method of an Internet-facing SLB instance. The following billing methods are supported:
        # 
        # *   **PayBySpec**: Pay-by-specification.
        # *   **PayByCLCU**: Pay-by-CLCU.
        self.internet_slb_charge_type = internet_slb_charge_type
        # lb-bp1tg0k6d9nqaw7l1\\*\\*\\*\\*
        self.internet_slb_id = internet_slb_id
        # [{"port":80,"targetPort":8080,"protocol":"TCP"}]
        self.intranet = intranet
        # The billing method of an Internal-facing SLB instance. The following billing methods are supported:
        # 
        # *   **PayBySpec**: Pay-by-specification.
        # *   **PayByCLCU**: Pay-by-CLCU.
        self.intranet_slb_charge_type = intranet_slb_charge_type
        # lb-bp1tg0k6d9nqaw7l1\\*\\*\\*\\*
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.internet is not None:
            result['Internet'] = self.internet

        if self.internet_slb_charge_type is not None:
            result['InternetSlbChargeType'] = self.internet_slb_charge_type

        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id

        if self.intranet is not None:
            result['Intranet'] = self.intranet

        if self.intranet_slb_charge_type is not None:
            result['IntranetSlbChargeType'] = self.intranet_slb_charge_type

        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Internet') is not None:
            self.internet = m.get('Internet')

        if m.get('InternetSlbChargeType') is not None:
            self.internet_slb_charge_type = m.get('InternetSlbChargeType')

        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')

        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')

        if m.get('IntranetSlbChargeType') is not None:
            self.intranet_slb_charge_type = m.get('IntranetSlbChargeType')

        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')

        return self

