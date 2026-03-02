# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcReview(DaraModel):
    def __init__(
        self,
        developer_id: int = None,
        developer_name: str = None,
        feedback_pbc_api: str = None,
        feedback_pbc_instruction: str = None,
        feedback_pbc_schema: str = None,
        feedback_security: str = None,
        feedback_service_available: str = None,
        id: int = None,
        market_id: int = None,
        market_name: str = None,
        pbc_name: str = None,
        pbc_url: str = None,
        pbc_version: str = None,
        remain_time: str = None,
        request_id: str = None,
        reviewer_id: int = None,
        status: str = None,
    ):
        self.developer_id = developer_id
        self.developer_name = developer_name
        self.feedback_pbc_api = feedback_pbc_api
        self.feedback_pbc_instruction = feedback_pbc_instruction
        self.feedback_pbc_schema = feedback_pbc_schema
        self.feedback_security = feedback_security
        self.feedback_service_available = feedback_service_available
        self.id = id
        # This parameter is required.
        self.market_id = market_id
        self.market_name = market_name
        # This parameter is required.
        self.pbc_name = pbc_name
        # This parameter is required.
        self.pbc_url = pbc_url
        # This parameter is required.
        self.pbc_version = pbc_version
        self.remain_time = remain_time
        self.request_id = request_id
        # This parameter is required.
        self.reviewer_id = reviewer_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.developer_name is not None:
            result['developerName'] = self.developer_name

        if self.feedback_pbc_api is not None:
            result['feedbackPbcApi'] = self.feedback_pbc_api

        if self.feedback_pbc_instruction is not None:
            result['feedbackPbcInstruction'] = self.feedback_pbc_instruction

        if self.feedback_pbc_schema is not None:
            result['feedbackPbcSchema'] = self.feedback_pbc_schema

        if self.feedback_security is not None:
            result['feedbackSecurity'] = self.feedback_security

        if self.feedback_service_available is not None:
            result['feedbackServiceAvailable'] = self.feedback_service_available

        if self.id is not None:
            result['id'] = self.id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.market_name is not None:
            result['marketName'] = self.market_name

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.pbc_url is not None:
            result['pbcUrl'] = self.pbc_url

        if self.pbc_version is not None:
            result['pbcVersion'] = self.pbc_version

        if self.remain_time is not None:
            result['remainTime'] = self.remain_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('developerName') is not None:
            self.developer_name = m.get('developerName')

        if m.get('feedbackPbcApi') is not None:
            self.feedback_pbc_api = m.get('feedbackPbcApi')

        if m.get('feedbackPbcInstruction') is not None:
            self.feedback_pbc_instruction = m.get('feedbackPbcInstruction')

        if m.get('feedbackPbcSchema') is not None:
            self.feedback_pbc_schema = m.get('feedbackPbcSchema')

        if m.get('feedbackSecurity') is not None:
            self.feedback_security = m.get('feedbackSecurity')

        if m.get('feedbackServiceAvailable') is not None:
            self.feedback_service_available = m.get('feedbackServiceAvailable')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('marketName') is not None:
            self.market_name = m.get('marketName')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('pbcUrl') is not None:
            self.pbc_url = m.get('pbcUrl')

        if m.get('pbcVersion') is not None:
            self.pbc_version = m.get('pbcVersion')

        if m.get('remainTime') is not None:
            self.remain_time = m.get('remainTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

