# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserCreditUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        credit_limit: str = None,
        message: str = None,
        remaining_credits: str = None,
        request_id: str = None,
        shadow_credit_limit: str = None,
        shadow_remaining_credits: str = None,
        shadow_used_credits: str = None,
        tenant_id: int = None,
        used_credits: str = None,
        user_id: int = None,
    ):
        # The error code.
        self.code = code
        # The credit limit of the user.
        self.credit_limit = credit_limit
        # The status code description.
        self.message = message
        # The remaining credits in real time.
        self.remaining_credits = remaining_credits
        # The request ID.
        self.request_id = request_id
        # The shadow credit limit.
        self.shadow_credit_limit = shadow_credit_limit
        # The remaining shadow credits in real time.
        self.shadow_remaining_credits = shadow_remaining_credits
        # The consumed shadow credits in real time.
        self.shadow_used_credits = shadow_used_credits
        # The ID of the tenant to which the task belongs.
        self.tenant_id = tenant_id
        # The consumed credits in real time.
        self.used_credits = used_credits
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.credit_limit is not None:
            result['creditLimit'] = self.credit_limit

        if self.message is not None:
            result['message'] = self.message

        if self.remaining_credits is not None:
            result['remainingCredits'] = self.remaining_credits

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.shadow_credit_limit is not None:
            result['shadowCreditLimit'] = self.shadow_credit_limit

        if self.shadow_remaining_credits is not None:
            result['shadowRemainingCredits'] = self.shadow_remaining_credits

        if self.shadow_used_credits is not None:
            result['shadowUsedCredits'] = self.shadow_used_credits

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.used_credits is not None:
            result['usedCredits'] = self.used_credits

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('creditLimit') is not None:
            self.credit_limit = m.get('creditLimit')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('remainingCredits') is not None:
            self.remaining_credits = m.get('remainingCredits')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('shadowCreditLimit') is not None:
            self.shadow_credit_limit = m.get('shadowCreditLimit')

        if m.get('shadowRemainingCredits') is not None:
            self.shadow_remaining_credits = m.get('shadowRemainingCredits')

        if m.get('shadowUsedCredits') is not None:
            self.shadow_used_credits = m.get('shadowUsedCredits')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('usedCredits') is not None:
            self.used_credits = m.get('usedCredits')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

