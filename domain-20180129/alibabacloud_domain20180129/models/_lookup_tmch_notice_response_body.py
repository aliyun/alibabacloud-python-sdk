# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class LookupTmchNoticeResponseBody(DaraModel):
    def __init__(
        self,
        claims: main_models.LookupTmchNoticeResponseBodyClaims = None,
        id: int = None,
        label: str = None,
        not_after: str = None,
        not_before: str = None,
        request_id: str = None,
    ):
        self.claims = claims
        self.id = id
        self.label = label
        self.not_after = not_after
        self.not_before = not_before
        self.request_id = request_id

    def validate(self):
        if self.claims:
            self.claims.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claims is not None:
            result['Claims'] = self.claims.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Claims') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaims()
            self.claims = temp_model.from_map(m.get('Claims'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class LookupTmchNoticeResponseBodyClaims(DaraModel):
    def __init__(
        self,
        claim: List[main_models.LookupTmchNoticeResponseBodyClaimsClaim] = None,
    ):
        self.claim = claim

    def validate(self):
        if self.claim:
            for v1 in self.claim:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Claim'] = []
        if self.claim is not None:
            for k1 in self.claim:
                result['Claim'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.claim = []
        if m.get('Claim') is not None:
            for k1 in m.get('Claim'):
                temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaim()
                self.claim.append(temp_model.from_map(k1))

        return self

class LookupTmchNoticeResponseBodyClaimsClaim(DaraModel):
    def __init__(
        self,
        class_descs: main_models.LookupTmchNoticeResponseBodyClaimsClaimClassDescs = None,
        contacts: main_models.LookupTmchNoticeResponseBodyClaimsClaimContacts = None,
        goods_and_services: str = None,
        holders: main_models.LookupTmchNoticeResponseBodyClaimsClaimHolders = None,
        jur_desc: main_models.LookupTmchNoticeResponseBodyClaimsClaimJurDesc = None,
        mark_name: str = None,
    ):
        self.class_descs = class_descs
        self.contacts = contacts
        self.goods_and_services = goods_and_services
        self.holders = holders
        self.jur_desc = jur_desc
        self.mark_name = mark_name

    def validate(self):
        if self.class_descs:
            self.class_descs.validate()
        if self.contacts:
            self.contacts.validate()
        if self.holders:
            self.holders.validate()
        if self.jur_desc:
            self.jur_desc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_descs is not None:
            result['ClassDescs'] = self.class_descs.to_map()

        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()

        if self.goods_and_services is not None:
            result['GoodsAndServices'] = self.goods_and_services

        if self.holders is not None:
            result['Holders'] = self.holders.to_map()

        if self.jur_desc is not None:
            result['JurDesc'] = self.jur_desc.to_map()

        if self.mark_name is not None:
            result['MarkName'] = self.mark_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassDescs') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimClassDescs()
            self.class_descs = temp_model.from_map(m.get('ClassDescs'))

        if m.get('Contacts') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimContacts()
            self.contacts = temp_model.from_map(m.get('Contacts'))

        if m.get('GoodsAndServices') is not None:
            self.goods_and_services = m.get('GoodsAndServices')

        if m.get('Holders') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimHolders()
            self.holders = temp_model.from_map(m.get('Holders'))

        if m.get('JurDesc') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimJurDesc()
            self.jur_desc = temp_model.from_map(m.get('JurDesc'))

        if m.get('MarkName') is not None:
            self.mark_name = m.get('MarkName')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimJurDesc(DaraModel):
    def __init__(
        self,
        desc: str = None,
        jur_cc: str = None,
    ):
        self.desc = desc
        self.jur_cc = jur_cc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.jur_cc is not None:
            result['JurCC'] = self.jur_cc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('JurCC') is not None:
            self.jur_cc = m.get('JurCC')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimHolders(DaraModel):
    def __init__(
        self,
        holder: List[main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder] = None,
    ):
        self.holder = holder

    def validate(self):
        if self.holder:
            for v1 in self.holder:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Holder'] = []
        if self.holder is not None:
            for k1 in self.holder:
                result['Holder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.holder = []
        if m.get('Holder') is not None:
            for k1 in m.get('Holder'):
                temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder()
                self.holder.append(temp_model.from_map(k1))

        return self

class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder(DaraModel):
    def __init__(
        self,
        addr: main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr = None,
        entitlement: str = None,
        org: str = None,
    ):
        self.addr = addr
        self.entitlement = entitlement
        self.org = org

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()

        if self.entitlement is not None:
            result['Entitlement'] = self.entitlement

        if self.org is not None:
            result['Org'] = self.org

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr()
            self.addr = temp_model.from_map(m.get('Addr'))

        if m.get('Entitlement') is not None:
            self.entitlement = m.get('Entitlement')

        if m.get('Org') is not None:
            self.org = m.get('Org')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr(DaraModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        pc: str = None,
        sp: str = None,
        street: main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet = None,
    ):
        self.cc = cc
        self.city = city
        self.pc = pc
        self.sp = sp
        self.street = street

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc is not None:
            result['Cc'] = self.cc

        if self.city is not None:
            result['City'] = self.city

        if self.pc is not None:
            result['Pc'] = self.pc

        if self.sp is not None:
            result['Sp'] = self.sp

        if self.street is not None:
            result['Street'] = self.street.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Pc') is not None:
            self.pc = m.get('Pc')

        if m.get('Sp') is not None:
            self.sp = m.get('Sp')

        if m.get('Street') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet()
            self.street = temp_model.from_map(m.get('Street'))

        return self

class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet(DaraModel):
    def __init__(
        self,
        street: List[str] = None,
    ):
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.street is not None:
            result['Street'] = self.street

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimContacts(DaraModel):
    def __init__(
        self,
        contact: List[main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContact] = None,
    ):
        self.contact = contact

    def validate(self):
        if self.contact:
            for v1 in self.contact:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contact'] = []
        if self.contact is not None:
            for k1 in self.contact:
                result['Contact'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k1 in m.get('Contact'):
                temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContact()
                self.contact.append(temp_model.from_map(k1))

        return self

class LookupTmchNoticeResponseBodyClaimsClaimContactsContact(DaraModel):
    def __init__(
        self,
        addr: main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr = None,
        email: str = None,
        fax: str = None,
        name: str = None,
        org: str = None,
        type: str = None,
        voice: str = None,
    ):
        self.addr = addr
        self.email = email
        self.fax = fax
        self.name = name
        self.org = org
        self.type = type
        self.voice = voice

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()

        if self.email is not None:
            result['Email'] = self.email

        if self.fax is not None:
            result['Fax'] = self.fax

        if self.name is not None:
            result['Name'] = self.name

        if self.org is not None:
            result['Org'] = self.org

        if self.type is not None:
            result['Type'] = self.type

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr()
            self.addr = temp_model.from_map(m.get('Addr'))

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Fax') is not None:
            self.fax = m.get('Fax')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Org') is not None:
            self.org = m.get('Org')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr(DaraModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        pc: str = None,
        sp: str = None,
        street: main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet = None,
    ):
        self.cc = cc
        self.city = city
        self.pc = pc
        self.sp = sp
        self.street = street

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc is not None:
            result['Cc'] = self.cc

        if self.city is not None:
            result['City'] = self.city

        if self.pc is not None:
            result['Pc'] = self.pc

        if self.sp is not None:
            result['Sp'] = self.sp

        if self.street is not None:
            result['Street'] = self.street.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Pc') is not None:
            self.pc = m.get('Pc')

        if m.get('Sp') is not None:
            self.sp = m.get('Sp')

        if m.get('Street') is not None:
            temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet()
            self.street = temp_model.from_map(m.get('Street'))

        return self

class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet(DaraModel):
    def __init__(
        self,
        street: List[str] = None,
    ):
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.street is not None:
            result['Street'] = self.street

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')

        return self

class LookupTmchNoticeResponseBodyClaimsClaimClassDescs(DaraModel):
    def __init__(
        self,
        class_desc: List[main_models.LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc] = None,
    ):
        self.class_desc = class_desc

    def validate(self):
        if self.class_desc:
            for v1 in self.class_desc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClassDesc'] = []
        if self.class_desc is not None:
            for k1 in self.class_desc:
                result['ClassDesc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_desc = []
        if m.get('ClassDesc') is not None:
            for k1 in m.get('ClassDesc'):
                temp_model = main_models.LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc()
                self.class_desc.append(temp_model.from_map(k1))

        return self

class LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc(DaraModel):
    def __init__(
        self,
        class_num: int = None,
        desc: str = None,
    ):
        self.class_num = class_num
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_num is not None:
            result['ClassNum'] = self.class_num

        if self.desc is not None:
            result['Desc'] = self.desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        return self

