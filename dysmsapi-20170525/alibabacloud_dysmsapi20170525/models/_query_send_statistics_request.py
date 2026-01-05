# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySendStatisticsRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        is_globe: int = None,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        start_date: str = None,
        template_type: int = None,
    ):
        # The end of the time range to query. Format: yyyyMMdd. Example: 20181225.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The site from where the message is sent. Valid values:
        # 
        # *   **1**: China site
        # *   **2**: international site
        # 
        # This parameter is required.
        self.is_globe = is_globe
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        # 
        # This parameter is required.
        self.page_index = page_index
        # The number of entries to return on each page. Valid values: **1 to 50**.
        # 
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature.
        self.sign_name = sign_name
        # The beginning of the time range to query. Format: yyyyMMdd. Example: 20181225.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The type of the message template. Valid values: Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification
        # *   **2**: promotional message (Enterprise users only)
        # *   **3**: international purpose (Enterprise users only)
        # *   **7**: digital message
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.is_globe is not None:
            result['IsGlobe'] = self.is_globe

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('IsGlobe') is not None:
            self.is_globe = m.get('IsGlobe')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

