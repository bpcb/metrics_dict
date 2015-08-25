metrics_dict = {
	"SignedInUus": """
		COUNT(distinct CASE WHEN zuid is not null THEN zuid END)
		""",
	"Visits": """
		COUNT(distinct uniquesessionid)
		""",
	"Pvs": """
		SUM(CASE WHEN hitstype = 'PAGE' THEN 1 
			ELSE 0 END)
		""",
	"HdpPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND customdimension2value is not null THEN 1 
			ELSE 0 END)
		""",
	"FSHdpPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND customdimension2value is not null AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
			ELSE 0 END)
		""",
	"FRHdpPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND strpos(lower(customdimension14value),'rent') > 0 THEN 1 
			ELSE 0 END)
		""",
	"FRBuildingPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND strpos(lower(customdimension14value),'building') > 0 AND strpos(lower(customdimension15value), 'rent') > 0 THEN 1 
			ELSE 0 END)
		""",
	"PMFHdpPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND strpos(lower(customdimension14value), 'rent') > 0 AND customdimension24value in ('featured-refreshed', 'refreshed') THEN 1 
			ELSE 0 END)
		""",
	"PMFBuildingPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' AND strpos(lower(customdimension14value), 'building') > 0 AND customdimension24value in ('featured-refreshed', 'refreshed') THEN 1 
			ELSE 0 END)""",
	"Submits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') THEN 1 
				ELSE 0 END)
		""",
	"DistinctSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' and hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') THEN uniquevisitorid END)
		""",
	"EmailSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' THEN 1 
			ELSE 0 END)
		""",
	"DistinctEmailSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' and hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' THEN uniquevisitorid END)
		""",
	"PhoneSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' THEN 1 
			ELSE 0 END)
		""",
	"DistinctPhoneSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' and hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' THEN uniquevisitorid END)
		""",
	"FSSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctFSSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') 
					AND strpos(lower(customdimension14value),'sale') > 0 THEN uniquevisitorid END)
		""",
	"FSEmailSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctFSEmailSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND strpos(lower(customdimension14value),'sale') > 0 THEN uniquevisitorid END)
		""",
	"FSPhoneSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
					AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctFSPhoneSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
					AND strpos(lower(customdimension14value),'sale') > 0 THEN uniquevisitorid END)
		""",
	"FRSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN 1 
			ELSE 0 END)
		
		""",
	"DistinctFRSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN uniquevisitorid END)
		""",
	"FREmailSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctFREmailSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN uniquevisitorid END)
		""",
	"FRPhoneSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctFRPhoneSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
					AND strpos(lower(customdimension14value),'rent') > 0 THEN uniquevisitorid END)
		""",
	"PMFSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') 
					AND customdimension24value in ('featured-refreshed', 'refreshed') THEN 1 
			ELSE 0 END)
		""",
	"DistinctPMFSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction in ('call', 'email') 
					AND customdimension24value in ('featured-refreshed', 'refreshed') THEN uniquevisitorid END)
		""",
	"PMFEmailSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND customdimension24value in ('featured-refreshed', 'refreshed') THEN 1 
			ELSE 0 END)
		""",
	"DistinctPMFEmailSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND customdimension24value in ('featured-refreshed', 'refreshed') THEN uniquevisitorid END)
		""",
	"PMFPhoneSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
					AND customdimension24value in ('featured-refreshed', 'refreshed') THEN 1 
			ELSE 0 END)""",
	"DistinctPMFPhoneSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'call' 
				AND customdimension24value in ('featured-refreshed', 'refreshed') THEN uniquevisitorid END)
		""",
	"DirectoryPVs": """
	    SUM(CASE WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'/directory/') > 0 THEN 1
            WHEN strpos(lower(hitspagepagepath),'/agent-finder/') > 0 THEN 1
            WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'real-estate-agent-reviews') > 0 THEN 1
            WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'mortgage-lender-reviews') > 0 THEN 1
            WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'home-improvement-reviews') > 0 THEN 1
            WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'property-manager-reviews') > 0 THEN 1
            WHEN l0.hitstype = 'PAGE' AND strpos(lower(hitspagepagepath),'real-estate-services-reviews') > 0 THEN 1
            ELSE 0 END)
	    """,
	"ProfilePvs": """
	    SUM(CASE WHEN l0.hitstype = 'PAGE' AND strpos(hitspagepagepath, 'profile') > 0 THEN 1 
	    	ELSE 0 END)
        """,
	"ProfileSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' AND  hitseventinfocategory = 'Contact-Agent' AND hitseventinfoaction = 'Form Submit' 
					AND strpos(hitseventinfolabel,'Profile') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DistinctProfileSubmits": """
		COUNT(DISTINCT CASE WHEN hitstype = 'EVENT' AND  hitseventinfocategory = 'Contact-Agent' AND hitseventinfoaction = 'Form Submit' 
					AND strpos(hitseventinfolabel,'Profile') > 0 THEN uniquevisitorid END)
		""",
	"ListingAgentSelectedEmailSubmit": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' AND 
				SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' AND LEFT(SPLIT_PART(hitseventinfolabel, '/', 3),1) = 1 THEN 1 
			ELSE 0 END)
		""",
	"BAL4EmailSubmit": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
					AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' THEN 1 
				ELSE 0 END)
		""",
	"Registrations": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory in ('Register', 'Auth') 
					AND hitseventinfoaction in ('Auth success - register - email - non-pro','Auth success - register - email - pro',
												'Auth success - register - FB - non-pro','Auth success - register - FB - pro') THEN 1 
			ELSE 0 END)
		""",
	"HomeSaves": """
		SUM(CASE WHEN hitstype = 'EVENT' AND ((hitseventinfocategory = 'Alerts' AND hitseventinfoaction = 'Property Report' AND hitseventinfolabel = 'Save') 
					OR (hitseventinfocategory = 'Followed Homes' AND hitseventinfoaction = 'Follow Home' AND strpos(hitseventinfolabel,'Action Bar')>0)) THEN 1 
			ELSE 0 END)
		""",
	"PhotoLightboxOpen": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction = 'Photo Lighbtox - Open' AND customdimension25value in ('Desktop', 'Tablet') THEN 1 
			ELSE 0 END)
		""",
	"MortgageCalcClick": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Mortgages' AND hitseventinfoaction = 'HDP:HeaderCalculator' 
				AND hitseventinfolabel = 'Form Activated' THEN 1 
			ELSE 0 END)
		""",
	"ContactButtoninActionBar": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Homes' AND hitseventinfoaction = 'Contact-Anchor' 
					AND customdimension25value in ('Phone') THEN 1 
			ELSE 0 END)
		""",
	"DigsPvs": """
		SUM(CASE WHEN hitstype = 'PAGE' and strpos(hitspagepagepath, 'digs') > 0 THEN 1 
			ELSE 0 END)
		""",
	"DigsSubmits": """
		SUM(CASE WHEN hitstype = 'EVENT' and hitseventinfoaction = 'dig submit' and hitseventinfocategory = 'digs' THEN 1 
			ELSE 0 END)
		""",
	"DigsUus": """
		COUNT(distinct CASE WHEN strpos(hitspagepagepath, 'digs') > 0 THEN uniquevisitorid END)
		""",
	"ZMMUus": """
		COUNT(distinct CASE WHEN (strpos(hitspagepagepath, '/mortgage-rates/') = 1 OR strpos(hitspagepagepath, '/refinance/') = 1) THEN uniquevisitorid END)
		""",
	"ZMMLoanRequests": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Mortgages' AND (hitseventinfoaction = 'Loan Request' 
					OR (hitseventinfoaction = 'Mobile Web' and strpos(hitseventinfolabel, 'Loan Request') > 0)) THEN 1 
			ELSE 0 END)
		""",
	"ZMMQdpClicks": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Mortgages' AND (hitseventinfoaction = 'QDP' 
					OR (hitseventinfoaction = 'Mobile Web' and hitseventinfolabel = 'Quote Card Click')) THEN 1 
			ELSE 0 END)
		""",
	"ZMMLenderWebsiteClicks": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Mortgages' AND hitseventinfoaction = 'ZMM Lender - website click' THEN 1 
			ELSE 0 END)
		""",
	"ZMMContacts": """
		SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'Mortgages' AND hitseventinfoaction = 'ZMM Contact - form submit' THEN 1 
			ELSE 0 END)
		""",
	"PreApprovalUus": """
		COUNT(distinct CASE WHEN strpos(hitspagepagepath, '/pre-approval/') = 1 THEN uniquevisitorid END)
		""",
    "PreApprovalGetStarted": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND hitspagepagepath = '/pre-approval/' AND hitseventinfocategory = 'Mortgages' 
    				AND hitseventinfoaction = 'Next clicked' AND hitseventinfolabel = 'Preapproval Landing' THEN 1 
    		ELSE 0 END)
		""",
    "PreApprovalCompleted": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND strpos(hitspagepagepath, '/pre-approval/') = 1 AND hitseventinfocategory = 'Mortgages' 
    				AND hitseventinfoaction = 'completed process' AND hitseventinfolabel = 'PreapprovalWizard' THEN 1 
    		ELSE 0 END)
		""",
    "PreApprovalValuedContacts": """
    	SUM(CASE WHEN hitstype = 'PAGE' AND strpos(hitspagepagepath, '/pre-approval/') = 1 AND strpos(hitspagepagepath, 'final') > 0 
    				AND strpos(hitspagepagepath, '-sc') = 0 THEN 1 
    		ELSE 0 END)
		""",
    "DistinctZPROSubmits": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction in ('call','email') AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' 
    				AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
    		ELSE 0 END)
		""",
    "DistinctZPROEmailSubmits": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction = 'email' AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' 
    				AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
    		ELSE 0 END)
		""",
    "DistinctZPROPhoneSubmits": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction = 'call' AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' 
    				AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
    		ELSE 0 END)
		""",
    "DistinctZPROSubmitsToListingAgent": """
    	SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfocategory = 'contact' AND hitseventinfoaction = 'email' 
    				AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4' AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 
    				AND LEFT(SPLIT_PART(hitseventinfolabel, '/', 3),1) = 1 AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
    		ELSE 0 END)
		""",
    "DistinctZPROSubmitsToNonListingAgent": """
        SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction in ('call', 'email') AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4'
        			AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 AND right(SPLIT_PART(hitseventinfolabel, '/', 3),3) <> '000'
        			AND strpos(lower(customdimension14value),'sale') > 0 THEN 1 
        	ELSE 0 END)
        """,
    "DistinctZPROEmailSubmitsToNonListingAgent": """
        SUM(CASE WHEN hitstype = 'EVENT' AND hitseventinfoaction = 'email' AND SPLIT_PART(customdimension27value, '\\\\', 1) = 'bal4'
        		AND right(SPLIT_PART(customdimension27value,'\\\\',  5),1) = 1 AND right(SPLIT_PART(hitseventinfolabel, '/', 3),3) <> '000' THEN 1 
        	ELSE 0 END)
        """
}
