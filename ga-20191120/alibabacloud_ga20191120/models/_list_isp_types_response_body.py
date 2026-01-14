# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListIspTypesResponseBody(DaraModel):
    def __init__(
        self,
        isp_type_list: List[str] = None,
        request_id: str = None,
    ):
        # The line types of EIPs in the acceleration region.
        # 
        # *   **BGP** (default): BGP (Multi-ISP) lines
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines
        # 
        # If you have the permissions to use single-ISP bandwidth, one of the following values may be returned:
        # 
        # *   **ChinaTelecom**: China Telecom (single ISP)
        # *   **ChinaUnicom**: China Unicom (single ISP)
        # *   **ChinaMobile**: China Mobile (single ISP)
        # *   **ChinaTelecom_L2**: China Telecom_L2 (single ISP)
        # *   **ChinaUnicom_L2**: China Unicom_L2 (single ISP)
        # *   **ChinaMobile_L2**: China Mobile_L2 (single ISP)
        # 
        # > Different acceleration regions support different single-ISP BGP lines.
        self.isp_type_list = isp_type_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp_type_list is not None:
            result['IspTypeList'] = self.isp_type_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspTypeList') is not None:
            self.isp_type_list = m.get('IspTypeList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

