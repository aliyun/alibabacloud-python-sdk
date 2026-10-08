# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryAdvancedDomainListRequest(DaraModel):
    def __init__(
        self,
        domain_group_id: int = None,
        domain_name_sort: bool = None,
        domain_status: int = None,
        end_expiration_date: int = None,
        end_length: int = None,
        end_registration_date: int = None,
        excluded: str = None,
        excluded_prefix: bool = None,
        excluded_suffix: bool = None,
        expiration_date_sort: bool = None,
        form: int = None,
        is_premium_domain: bool = None,
        key_word: str = None,
        key_word_prefix: bool = None,
        key_word_suffix: bool = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        product_domain_type: str = None,
        product_domain_type_sort: bool = None,
        registration_date_sort: bool = None,
        resource_group_id: str = None,
        start_expiration_date: int = None,
        start_length: int = None,
        start_registration_date: int = None,
        suffixs: str = None,
        tag: List[main_models.QueryAdvancedDomainListRequestTag] = None,
        trade_type: int = None,
        user_client_ip: str = None,
    ):
        # Domain group ID.
        self.domain_group_id = domain_group_id
        # Sorting field based on lexicographic order of domain names. Valid values:  
        # - **false**: Descending order  
        # - **true**: Ascending order
        self.domain_name_sort = domain_name_sort
        # Domain status. Valid values:
        # - **0**: All.
        # - **1**: Renewal required urgently.
        # - **2**: Redemption required urgently.
        # - **3**: Normal.
        # - **4**: Transferring out from HiChina.
        # - **5**: Registrant information being modified.
        # - **6**: Identity verification not completed.
        # - **7**: Review failed; re-initiate identity verification.
        # - **8**: Under review.
        self.domain_status = domain_status
        # End time for expiration date range query, represented as the number of milliseconds since 00:00:00 UTC on January 1, 1970.
        self.end_expiration_date = end_expiration_date
        # End length for domain name length range query.
        self.end_length = end_length
        # The end time of the registration date range query, expressed as the number of milliseconds since 00:00 on January 1, 1970, UTC.
        self.end_registration_date = end_registration_date
        # Excluded keyword.
        self.excluded = excluded
        # Keyword to exclude at the beginning.
        self.excluded_prefix = excluded_prefix
        # Keyword to exclude at the end.
        self.excluded_suffix = excluded_suffix
        # Sorting field based on expiration date. Valid values:
        # - **false**: Descending order.
        # - **true**: Ascending order.
        self.expiration_date_sort = expiration_date_sort
        # Domain name composition information:  
        # - **11**: Numeric-only domain name  
        # - **12**: Letter-only domain name  
        # - **13**: Mixed domain name (combination of letters and numbers)  
        # - **14**: Chinese domain name
        self.form = form
        # Indicates whether the domain is a premium domain. Valid values:  
        # - **false**: No  
        # - **true**: Yes  
        # 
        # Default value: false.
        self.is_premium_domain = is_premium_domain
        # Keyword.
        self.key_word = key_word
        # Keyword at the beginning.
        self.key_word_prefix = key_word_prefix
        # Keyword at the end.
        self.key_word_suffix = key_word_suffix
        # The language of error messages returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # Page number for paging. The minimum value is **0**.
        # 
        # This parameter is required.
        self.page_num = page_num
        # Page size for paging. The minimum value is **1** and the maximum value is **200**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Domain name type. Valid values:
        # - **New gTLD** (new top-level domain).
        # - **gTLD** (generic top-level domain).
        # - **ccTLD** (country code top-level domain).
        # - **other** (other top-level domains not listed above).
        self.product_domain_type = product_domain_type
        # Sorting field, used to sort by domain name type. Valid values:
        # - **false**: Descending order.
        # - **true**: Ascending order.
        self.product_domain_type_sort = product_domain_type_sort
        # Sorting field based on registration date. Valid values:
        # - **false**: Descending order.
        # - **true**: Ascending order.
        self.registration_date_sort = registration_date_sort
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Start time for expiration date range query, represented as the number of milliseconds since 00:00:00 UTC on January 1, 1970.
        self.start_expiration_date = start_expiration_date
        # The starting length for domain name length range queries.
        self.start_length = start_length
        # The start time of the registration date range query, expressed as the number of milliseconds since 00:00 on January 1, 1970, UTC.
        self.start_registration_date = start_registration_date
        # List of suffixes to query, separated by commas (",").
        self.suffixs = suffixs
        # List of tags.
        self.tag = tag
        # Publishing status. Valid values:  
        # - **2**: Fixed-price listing published  
        # - **13**: Negotiable-price listing published  
        # - **4**: Auction listing published  
        # - **6**: Priced push listing published  
        # - **-1**: Domain trading not published
        self.trade_type = trade_type
        # User IP address.
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_name_sort is not None:
            result['DomainNameSort'] = self.domain_name_sort

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

        if self.expiration_date_sort is not None:
            result['ExpirationDateSort'] = self.expiration_date_sort

        if self.form is not None:
            result['Form'] = self.form

        if self.is_premium_domain is not None:
            result['IsPremiumDomain'] = self.is_premium_domain

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.key_word_prefix is not None:
            result['KeyWordPrefix'] = self.key_word_prefix

        if self.key_word_suffix is not None:
            result['KeyWordSuffix'] = self.key_word_suffix

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_domain_type is not None:
            result['ProductDomainType'] = self.product_domain_type

        if self.product_domain_type_sort is not None:
            result['ProductDomainTypeSort'] = self.product_domain_type_sort

        if self.registration_date_sort is not None:
            result['RegistrationDateSort'] = self.registration_date_sort

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date

        if self.start_length is not None:
            result['StartLength'] = self.start_length

        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date

        if self.suffixs is not None:
            result['Suffixs'] = self.suffixs

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.trade_type is not None:
            result['TradeType'] = self.trade_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainNameSort') is not None:
            self.domain_name_sort = m.get('DomainNameSort')

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

        if m.get('ExpirationDateSort') is not None:
            self.expiration_date_sort = m.get('ExpirationDateSort')

        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('IsPremiumDomain') is not None:
            self.is_premium_domain = m.get('IsPremiumDomain')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('KeyWordPrefix') is not None:
            self.key_word_prefix = m.get('KeyWordPrefix')

        if m.get('KeyWordSuffix') is not None:
            self.key_word_suffix = m.get('KeyWordSuffix')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductDomainType') is not None:
            self.product_domain_type = m.get('ProductDomainType')

        if m.get('ProductDomainTypeSort') is not None:
            self.product_domain_type_sort = m.get('ProductDomainTypeSort')

        if m.get('RegistrationDateSort') is not None:
            self.registration_date_sort = m.get('RegistrationDateSort')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')

        if m.get('StartLength') is not None:
            self.start_length = m.get('StartLength')

        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')

        if m.get('Suffixs') is not None:
            self.suffixs = m.get('Suffixs')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.QueryAdvancedDomainListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TradeType') is not None:
            self.trade_type = m.get('TradeType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

class QueryAdvancedDomainListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value of the instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

