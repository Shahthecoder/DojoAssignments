-- 1)
SELECT monthname(charged_datetime) as month, SUM(amount) as revenue
FROM billing
WHERE charged_datetime >= "2012-03-01" AND "2012-03-31";
-- 2)
SELECT client_id, SUM(amount) as total_rev
FROM billing
WHERE client_id = 2;
-- 3)
SELECT domain_name, client_id
FROM sites
WHERE client_id = 10;
-- 4)
SELECT client_id, COUNT(domain_name) as number_websites, MONTHNAME(created_datetime) as month_created, YEAR(created_datetime) as year_created
FROM sites
WHERE client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime)
ORDER BY created_datetime;
-- 5)
SELECT sites.domain_name as website, COUNT(leads.leads_id) as number_leads, DATE_FORMAT(leads.registered_datetime, "%M %d, %Y") as date_generated
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/02/15"
GROUP BY sites.site_id;
-- 6)
SELECT CONCAT(clients.first_name," ", clients.last_name) as client_name, COUNT(leads.leads_id) as number_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/12/31"
GROUP BY clients.client_id;
-- 7)
SELECT CONCAT(clients.first_name," ", clients.last_name) as client_name, COUNT(leads.leads_id) as number_leads, MONTHNAME(leads.registered_datetime) as month_generated
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/06/30"
GROUP BY leads.leads_id;
-- 8)
SELECT CONCAT(clients.first_name," ", clients.last_name) as client_name, COUNT(leads.leads_id) as number_leads
FROM leads
LEFT JOIN sites ON leads.site_id = sites.site_id
LEFT JOIN clients ON sites.client_id = clients.client_id
WHERE registered_datetime >= "2011/01/01" AND registered_datetime <= "2011/12/31"
GROUP BY sites.client_id, sites.site_id;
-- 9)
SELECT CONCAT(clients.first_name," ", clients.last_name) as client_name, SUM(billing.amount) as total_rev, MONTHNAME(billing.charged_datetime) as month_charged, YEAR(billing.charged_datetime) as year_charged
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, YEAR(billing.charged_datetime), MONTH(billing.charged_datetime);
-- 10)
SELECT CONCAT(clients.first_name," ", clients.last_name) as client_name, GROUP_CONCAT(sites.domain_name SEPARATOR "  /  ") as sites
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;



