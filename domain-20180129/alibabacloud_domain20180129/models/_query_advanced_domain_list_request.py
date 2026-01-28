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
        self.domain_group_id = domain_group_id
        self.domain_name_sort = domain_name_sort
        self.domain_status = domain_status
        self.end_expiration_date = end_expiration_date
        self.end_length = end_length
        self.end_registration_date = end_registration_date
        self.excluded = excluded
        self.excluded_prefix = excluded_prefix
        self.excluded_suffix = excluded_suffix
        self.expiration_date_sort = expiration_date_sort
        self.form = form
        self.is_premium_domain = is_premium_domain
        self.key_word = key_word
        self.key_word_prefix = key_word_prefix
        self.key_word_suffix = key_word_suffix
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.product_domain_type = product_domain_type
        self.product_domain_type_sort = product_domain_type_sort
        self.registration_date_sort = registration_date_sort
        self.resource_group_id = resource_group_id
        self.start_expiration_date = start_expiration_date
        self.start_length = start_length
        self.start_registration_date = start_registration_date
        self.suffixs = suffixs
        self.tag = tag
        self.trade_type = trade_type
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
        self.key = key
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

