# Overall (86/100)
 - Decent commit history - consider finer grained commits to better capture the
   flow of the project and make the history more navigable
 - You seem to have a very good handle on the computational aspects, for future
   labs make sure you devote more attention to the instrumentation aspects!

# Build (10/10)
 - Very detailed README - good
 - Note that when relying on an unstable external dependency (like becquerel)
   it is best to include the version or, better yet, the hash of the commit
   that you are relying on in that project

# Testing (10/10)
 - Testsuite did not run by default on my system due to dependency on 
   unittest.mock. Removed it and ran okay, though one test failed. See commit
   10a2034

# Intro / Background / Motivation (12/15)
 - Even for lab 0, the text is a bit vague - make sure to focus on the what and
   the why of the lab; i.e. energy calibration.
 - Providing context for the task at hand is an important component of 
   introducing the work. For example, the nature of pulse-height spectra, how
   they result from the signal processing chain, and how we can relate the
   features of spectra to gamma-ray energy deposition through via energy
   calibration.

# Methods (15/15)
 - Good details specific to analytic approach
 - An extention into uncertainty analysis would be straightforward from your
   presented equations

# Results and discussion (34/40)
 - Nice table for displaying the relevant data
 - Plots are well-made, but need more explanation in the text to draw out
   relevant components
 - You show values with much higher relative error compared to the other 
   evaluation targets - this behavior certainly warrants discussion!
 - Be careful with significant figures - you are claiming sub-eV precision when
   it is not warranted according to the nuclear data.
 - The "conclusion" score below mostly relates to the discussion

# Conclusion (5/10)
 - On the right track according to the "letter of the law", but an unsupported
   statement without further elaboration is 
