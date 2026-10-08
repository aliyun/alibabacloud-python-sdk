# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRegistrantProfileRealNameVerificationInfoRequest(DaraModel):
    def __init__(
        self,
        fetch_image: bool = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        # Specifies whether to retrieve the identity verification image. Valid values:  
        # - **true**: Retrieve the image.  
        # - **false**: Do not retrieve the image.  
        # 
        # Default value: **false**.
        self.fetch_image = fetch_image
        # The language of error messages returned by the API. Valid values:  
        # - **zh**: Chinese.  
        # - **en**: English.  
        # 
        # Default value: **en**.
        self.lang = lang
        # The ID of the information template to be queried.  
        # 
        # The system automatically generates this ID after the information template is created. You can call the [QueryRegistrantProfiles](https://help.aliyun.com/document_detail/67701.html) API to query the information template ID.
        # 
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        # The user IP address. You can set it to 127.0.0.1.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

