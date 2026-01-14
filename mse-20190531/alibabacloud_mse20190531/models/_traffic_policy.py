# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class TrafficPolicy(DaraModel):
    def __init__(
        self,
        load_balancer_settings: main_models.TrafficPolicyLoadBalancerSettings = None,
        tls_setting: main_models.TrafficPolicyTlsSetting = None,
    ):
        self.load_balancer_settings = load_balancer_settings
        self.tls_setting = tls_setting

    def validate(self):
        if self.load_balancer_settings:
            self.load_balancer_settings.validate()
        if self.tls_setting:
            self.tls_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_settings is not None:
            result['LoadBalancerSettings'] = self.load_balancer_settings.to_map()

        if self.tls_setting is not None:
            result['TlsSetting'] = self.tls_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerSettings') is not None:
            temp_model = main_models.TrafficPolicyLoadBalancerSettings()
            self.load_balancer_settings = temp_model.from_map(m.get('LoadBalancerSettings'))

        if m.get('TlsSetting') is not None:
            temp_model = main_models.TrafficPolicyTlsSetting()
            self.tls_setting = temp_model.from_map(m.get('TlsSetting'))

        return self

class TrafficPolicyTlsSetting(DaraModel):
    def __init__(
        self,
        ca_cert_content: str = None,
        cert_id: str = None,
        sni: str = None,
        tls_mode: str = None,
    ):
        self.ca_cert_content = ca_cert_content
        self.cert_id = cert_id
        self.sni = sni
        # This parameter is required.
        self.tls_mode = tls_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_content is not None:
            result['CaCertContent'] = self.ca_cert_content

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.sni is not None:
            result['Sni'] = self.sni

        if self.tls_mode is not None:
            result['TlsMode'] = self.tls_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertContent') is not None:
            self.ca_cert_content = m.get('CaCertContent')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('Sni') is not None:
            self.sni = m.get('Sni')

        if m.get('TlsMode') is not None:
            self.tls_mode = m.get('TlsMode')

        return self

class TrafficPolicyLoadBalancerSettings(DaraModel):
    def __init__(
        self,
        consistent_hash_lbconfig: main_models.TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig = None,
        loadbalancer_type: str = None,
        warmup_duration: int = None,
    ):
        self.consistent_hash_lbconfig = consistent_hash_lbconfig
        self.loadbalancer_type = loadbalancer_type
        self.warmup_duration = warmup_duration

    def validate(self):
        if self.consistent_hash_lbconfig:
            self.consistent_hash_lbconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistent_hash_lbconfig is not None:
            result['ConsistentHashLBConfig'] = self.consistent_hash_lbconfig.to_map()

        if self.loadbalancer_type is not None:
            result['LoadbalancerType'] = self.loadbalancer_type

        if self.warmup_duration is not None:
            result['WarmupDuration'] = self.warmup_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBConfig') is not None:
            temp_model = main_models.TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig()
            self.consistent_hash_lbconfig = temp_model.from_map(m.get('ConsistentHashLBConfig'))

        if m.get('LoadbalancerType') is not None:
            self.loadbalancer_type = m.get('LoadbalancerType')

        if m.get('WarmupDuration') is not None:
            self.warmup_duration = m.get('WarmupDuration')

        return self

class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig(DaraModel):
    def __init__(
        self,
        consistent_hash_lbtype: str = None,
        http_cookie: main_models.TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie = None,
        parameter_name: str = None,
    ):
        self.consistent_hash_lbtype = consistent_hash_lbtype
        self.http_cookie = http_cookie
        self.parameter_name = parameter_name

    def validate(self):
        if self.http_cookie:
            self.http_cookie.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistent_hash_lbtype is not None:
            result['ConsistentHashLBType'] = self.consistent_hash_lbtype

        if self.http_cookie is not None:
            result['HttpCookie'] = self.http_cookie.to_map()

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBType') is not None:
            self.consistent_hash_lbtype = m.get('ConsistentHashLBType')

        if m.get('HttpCookie') is not None:
            temp_model = main_models.TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie()
            self.http_cookie = temp_model.from_map(m.get('HttpCookie'))

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
        ttl: str = None,
    ):
        self.name = name
        self.path = path
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.ttl is not None:
            result['TTL'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        return self

