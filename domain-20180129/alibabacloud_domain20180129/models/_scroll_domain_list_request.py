# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScrollDomainListRequest(DaraModel):
    def __init__(
        self,
        domain_group_id: int = None,
        domain_status: int = None,
        end_expiration_date: int = None,
        end_length: int = None,
        end_registration_date: int = None,
        excluded: str = None,
        excluded_prefix: bool = None,
        excluded_suffix: bool = None,
        form: int = None,
        key_word: str = None,
        key_word_prefix: bool = None,
        key_word_suffix: bool = None,
        lang: str = None,
        page_size: int = None,
        product_domain_type: str = None,
        resource_group_id: str = None,
        scroll_id: str = None,
        start_expiration_date: int = None,
        start_length: int = None,
        start_registration_date: int = None,
        suffixs: str = None,
        trade_type: int = None,
        user_client_ip: str = None,
    ):
        # The ID of the domain name group. You can call the [QueryDomainGroupList](https://help.aliyun.com/document_detail/69362.html) operation to obtain the ID of the domain name group.
        self.domain_group_id = domain_group_id
        # The status of the domain name. Valid values:
        # 
        # *   **0**: All.
        # *   **1**: The domain name needs to be renewed.
        # *   **2**: The domain name needs to be redeemed.
        # *   **3**: The domain name is normal.
        # *   **4**: The domain name is being transferred from Alibaba Cloud.
        # *   **5**: The information about the domain name registrant is being modified.
        # *   **6**: Real-name verification is not performed on the domain name.
        # *   **7**: Real-name verification for the domain name fails. Real-name reverification is required.
        # *   **8**: The domain name is being reviewed.
        self.domain_status = domain_status
        # The end of the time range to query domain names based on expiration dates. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_expiration_date = end_expiration_date
        # The end of domain name length to query.
        self.end_length = end_length
        # The end of the time range to query domain names based on registration dates. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_registration_date = end_registration_date
        # The keyword that is used to exclude domain names.
        self.excluded = excluded
        # Specifies whether to exclude the prefix keyword.
        self.excluded_prefix = excluded_prefix
        # Specifies whether to exclude the suffix keyword.
        self.excluded_suffix = excluded_suffix
        # The composition of the domain name.
        self.form = form
        # The keyword.
        self.key_word = key_word
        # Specifies whether the keyword is the prefix.
        self.key_word_prefix = key_word_prefix
        # Specifies whether the keyword is the suffix.
        self.key_word_suffix = key_word_suffix
        # The language of the error message to return if the request fails. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The type of the domain name. Valid values:
        # 
        # *   **New gTLD**
        # *   **gTLD**
        # *   **ccTLD**
        # *   **other**
        self.product_domain_type = product_domain_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The scroll ID. This parameter is a technical parameter.
        self.scroll_id = scroll_id
        # The beginning of the time range to query domain names based on expiration dates. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_expiration_date = start_expiration_date
        # The start of the domain name length to query.
        self.start_length = start_length
        # The beginning of the time range to query domain names based on registration dates. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_registration_date = start_registration_date
        # The suffixes of domain names to be queried. Separate multiple suffixes with commas (,).
        self.suffixs = suffixs
        # The publishing status of the domain name. Valid values:
        # 
        # *   **2**: The domain name is published at a fixed price.
        # *   **3**: The domain name is published with the price negotiable.
        # *   **4**: The domain name is published for bidding.
        # *   **6**: The domain name is published with price push.
        # *   **-1**: The domain name is not published.
        self.trade_type = trade_type
        # The IP address of the client. Set the value to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.end_expiration_date is not None:
            result['EndExpirationDate'] = self.end_expiration_date

        if self.end_length is not None:
            result['EndLength'] = self.end_length

        if self.end_registration_date is not None:
            result['EndRegistrationDate'] = self.end_registration_date

        if self.excluded is not None:
            result['Excluded'] = self.excluded

        if self.excluded_prefix is not None:
            result['ExcludedPrefix'] = self.excluded_prefix

        if self.excluded_suffix is not None:
            result['ExcludedSuffix'] = self.excluded_suffix

        if self.form is not None:
            result['Form'] = self.form

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.key_word_prefix is not None:
            result['KeyWordPrefix'] = self.key_word_prefix

        if self.key_word_suffix is not None:
            result['KeyWordSuffix'] = self.key_word_suffix

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_domain_type is not None:
            result['ProductDomainType'] = self.product_domain_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scroll_id is not None:
            result['ScrollId'] = self.scroll_id

        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date

        if self.start_length is not None:
            result['StartLength'] = self.start_length

        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date

        if self.suffixs is not None:
            result['Suffixs'] = self.suffixs

        if self.trade_type is not None:
            result['TradeType'] = self.trade_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('EndExpirationDate') is not None:
            self.end_expiration_date = m.get('EndExpirationDate')

        if m.get('EndLength') is not None:
            self.end_length = m.get('EndLength')

        if m.get('EndRegistrationDate') is not None:
            self.end_registration_date = m.get('EndRegistrationDate')

        if m.get('Excluded') is not None:
            self.excluded = m.get('Excluded')

        if m.get('ExcludedPrefix') is not None:
            self.excluded_prefix = m.get('ExcludedPrefix')

        if m.get('ExcludedSuffix') is not None:
            self.excluded_suffix = m.get('ExcludedSuffix')

        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('KeyWordPrefix') is not None:
            self.key_word_prefix = m.get('KeyWordPrefix')

        if m.get('KeyWordSuffix') is not None:
            self.key_word_suffix = m.get('KeyWordSuffix')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductDomainType') is not None:
            self.product_domain_type = m.get('ProductDomainType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScrollId') is not None:
            self.scroll_id = m.get('ScrollId')

        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')

        if m.get('StartLength') is not None:
            self.start_length = m.get('StartLength')

        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')

        if m.get('Suffixs') is not None:
            self.suffixs = m.get('Suffixs')

        if m.get('TradeType') is not None:
            self.trade_type = m.get('TradeType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

