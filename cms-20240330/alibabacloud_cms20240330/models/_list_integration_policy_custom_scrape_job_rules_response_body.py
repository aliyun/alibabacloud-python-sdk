# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyCustomScrapeJobRulesResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        custom_scrape_job_rules: List[main_models.ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRules] = None,
        policy_id: str = None,
        request_id: str = None,
    ):
        # Cluster ID.
        self.cluster_id = cluster_id
        # Custom scraping job rules
        self.custom_scrape_job_rules = custom_scrape_job_rules
        # Policy ID.
        self.policy_id = policy_id
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.custom_scrape_job_rules:
            for v1 in self.custom_scrape_job_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        result['customScrapeJobRules'] = []
        if self.custom_scrape_job_rules is not None:
            for k1 in self.custom_scrape_job_rules:
                result['customScrapeJobRules'].append(k1.to_map() if k1 else None)

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        self.custom_scrape_job_rules = []
        if m.get('customScrapeJobRules') is not None:
            for k1 in m.get('customScrapeJobRules'):
                temp_model = main_models.ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRules()
                self.custom_scrape_job_rules.append(temp_model.from_map(k1))

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRules(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        addon_version: str = None,
        config_yaml: str = None,
        enable_status: str = None,
        encrypt_yaml: bool = None,
        matched_pod_count: int = None,
        message: str = None,
        name: str = None,
        namespace: str = None,
        scrape_configs: List[main_models.ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRulesScrapeConfigs] = None,
    ):
        # Addon name.
        self.addon_name = addon_name
        # Addon Release name
        self.addon_release_name = addon_release_name
        # Addon version
        self.addon_version = addon_version
        # Configuration yaml
        self.config_yaml = config_yaml
        # Enable status
        self.enable_status = enable_status
        # Encrypt yaml
        self.encrypt_yaml = encrypt_yaml
        # Matched pod count
        self.matched_pod_count = matched_pod_count
        # Detailed information.
        self.message = message
        # Service name.
        self.name = name
        # Namespace
        self.namespace = namespace
        # Custom configurations
        self.scrape_configs = scrape_configs

    def validate(self):
        if self.scrape_configs:
            for v1 in self.scrape_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.addon_release_name is not None:
            result['addonReleaseName'] = self.addon_release_name

        if self.addon_version is not None:
            result['addonVersion'] = self.addon_version

        if self.config_yaml is not None:
            result['configYaml'] = self.config_yaml

        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status

        if self.encrypt_yaml is not None:
            result['encryptYaml'] = self.encrypt_yaml

        if self.matched_pod_count is not None:
            result['matchedPodCount'] = self.matched_pod_count

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        result['scrapeConfigs'] = []
        if self.scrape_configs is not None:
            for k1 in self.scrape_configs:
                result['scrapeConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('addonReleaseName') is not None:
            self.addon_release_name = m.get('addonReleaseName')

        if m.get('addonVersion') is not None:
            self.addon_version = m.get('addonVersion')

        if m.get('configYaml') is not None:
            self.config_yaml = m.get('configYaml')

        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')

        if m.get('encryptYaml') is not None:
            self.encrypt_yaml = m.get('encryptYaml')

        if m.get('matchedPodCount') is not None:
            self.matched_pod_count = m.get('matchedPodCount')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        self.scrape_configs = []
        if m.get('scrapeConfigs') is not None:
            for k1 in m.get('scrapeConfigs'):
                temp_model = main_models.ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRulesScrapeConfigs()
                self.scrape_configs.append(temp_model.from_map(k1))

        return self

class ListIntegrationPolicyCustomScrapeJobRulesResponseBodyCustomScrapeJobRulesScrapeConfigs(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        message: str = None,
        metrics_path: str = None,
        scheme: str = None,
        scrape_interval: str = None,
        scrape_timeout: str = None,
        service_discovery_configs: List[str] = None,
    ):
        # Scraping job name
        self.job_name = job_name
        # Detailed information.
        self.message = message
        # Metrics path
        self.metrics_path = metrics_path
        # Call method.
        self.scheme = scheme
        # Scrape interval
        self.scrape_interval = scrape_interval
        # Scrape timeout
        self.scrape_timeout = scrape_timeout
        # Service discovery configuration
        self.service_discovery_configs = service_discovery_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.message is not None:
            result['message'] = self.message

        if self.metrics_path is not None:
            result['metricsPath'] = self.metrics_path

        if self.scheme is not None:
            result['scheme'] = self.scheme

        if self.scrape_interval is not None:
            result['scrapeInterval'] = self.scrape_interval

        if self.scrape_timeout is not None:
            result['scrapeTimeout'] = self.scrape_timeout

        if self.service_discovery_configs is not None:
            result['serviceDiscoveryConfigs'] = self.service_discovery_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metricsPath') is not None:
            self.metrics_path = m.get('metricsPath')

        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')

        if m.get('scrapeInterval') is not None:
            self.scrape_interval = m.get('scrapeInterval')

        if m.get('scrapeTimeout') is not None:
            self.scrape_timeout = m.get('scrapeTimeout')

        if m.get('serviceDiscoveryConfigs') is not None:
            self.service_discovery_configs = m.get('serviceDiscoveryConfigs')

        return self

