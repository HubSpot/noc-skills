package com.hubspot.NocSkillsAPI;

import com.yammer.metrics.core.HealthCheck;

public class NocSkillsAPIHealthCheck extends HealthCheck {
  public NocSkillsAPIHealthCheck() {
    super("NocSkills");
    // do nothing
  }
  
  @Override
  protected Result check() throws Exception {
    return Result.healthy();
  }
}
