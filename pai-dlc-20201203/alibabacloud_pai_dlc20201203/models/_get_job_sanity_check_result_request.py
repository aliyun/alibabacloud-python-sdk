# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobSanityCheckResultRequest(DaraModel):
    def __init__(
        self,
        sanity_check_number: int = None,
        sanity_check_phase: str = None,
        token: str = None,
    ):
        # The nth time for which the job sanity check is performed.
        # 
        # This parameter is required.
        self.sanity_check_number = sanity_check_number
        # The phase in which the job sanity check is performed.
        # 
        # *   CheckInit
        # *   DeviceCheck
        # *   SingleNodeCommCheck
        # *   TwoNodeCommCheck
        # *   AllNodeCommCheck
        self.sanity_check_phase = sanity_check_phase
        # The token information for job sharing. For more information about how to obtain the token information, see [GetToken](https://help.aliyun.com/document_detail/2557812.html).
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sanity_check_number is not None:
            result['SanityCheckNumber'] = self.sanity_check_number

        if self.sanity_check_phase is not None:
            result['SanityCheckPhase'] = self.sanity_check_phase

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SanityCheckNumber') is not None:
            self.sanity_check_number = m.get('SanityCheckNumber')

        if m.get('SanityCheckPhase') is not None:
            self.sanity_check_phase = m.get('SanityCheckPhase')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

